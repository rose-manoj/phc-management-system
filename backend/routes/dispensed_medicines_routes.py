from flask import Blueprint, jsonify, request
from services.dispensed_medicines_service import *
medicine_bp = Blueprint("medicine", __name__)

#GET ALL
@medicine_bp.route("/medicines", methods=["GET"])
def get_medicines():

    medicines = get_all_medicines()

    return jsonify(medicines)

#GET BY ID 
@medicine_bp.route("/medicines/<int:medicine_id>", methods=["GET"])
def get_medicine(medicine_id):

    medicine = get_medicine_by_id(medicine_id)

    if not medicine:
        return jsonify({
            "message": "Medicine not found"
        }),404

    return jsonify(medicine)

#POST
@medicine_bp.route("/medicines", methods=["POST"])
def create_medicine():

    data = request.get_json()

    required_fields = [
        "prescription_id",
        "medicine_name",
        "dosage",
        "quantity"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "message": f"{field} is required"
            }),400

    medicine_id = add_medicine(
        data["prescription_id"],
        data["medicine_name"],
        data["dosage"],
        data["quantity"]
    )

    return jsonify({
        "message":"Medicine added successfully",
        "medicine_id":medicine_id
    }),201

#PUT
@medicine_bp.route("/medicines/<int:medicine_id>", methods=["PUT"])
def edit_medicine(medicine_id):

    data = request.get_json()

    required_fields = [
        "prescription_id",
        "medicine_name",
        "dosage",
        "quantity"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "message":f"{field} is required"
            }),400

    rows = update_medicine(
        medicine_id,
        data["prescription_id"],
        data["medicine_name"],
        data["dosage"],
        data["quantity"]
    )

    if rows == 0:
        return jsonify({
            "message":"Medicine not found"
        }),404

    return jsonify({
        "message":"Medicine updated successfully"
    }),200

#DELETE
@medicine_bp.route("/medicines/<int:medicine_id>", methods=["DELETE"])
def remove_medicine(medicine_id):

    rows = delete_medicine(medicine_id)

    if rows == 0:
        return jsonify({
            "message":"Medicine not found"
        }),404

    return jsonify({
        "message":"Medicine deleted successfully"
    }),200