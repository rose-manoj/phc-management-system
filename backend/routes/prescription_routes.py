from flask import Blueprint, jsonify, request

from services.prescription_service import (
    get_all_prescriptions,
    get_prescription_by_id,
    add_prescription,
    update_prescription,
    delete_prescription
)

prescription_bp = Blueprint("prescription", __name__)

@prescription_bp.route("/prescriptions", methods=["GET"])
def get_prescriptions():

    prescriptions = get_all_prescriptions()

    prescription_list = []

    for p in prescriptions:
        prescription_list.append({
            "prescription_id": p[0],
            "patient_id": p[1],
            "prescription_date": str(p[2]),
            "lab_test_required": p[3]
        })

    return jsonify(prescription_list), 200

#GET BY ID 
@prescription_bp.route("/prescriptions/<int:prescription_id>", methods=["GET"])
def get_prescription(prescription_id):

    prescription = get_prescription_by_id(prescription_id)

    if not prescription:
        return jsonify({
            "message": "Prescription not found"
        }), 404

    return jsonify({
        "prescription_id": prescription[0],
        "patient_id": prescription[1],
        "prescription_date": str(prescription[2]),
        "lab_test_required": prescription[3]
    }), 200

#POST
@prescription_bp.route("/prescriptions", methods=["POST"])
def create_prescription():

    data = request.get_json()

    required_fields = [
        "patient_id",
        "prescription_date",
        "lab_test_required"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "message": f"{field} is required"
            }), 400

    prescription_id = add_prescription(
        data["patient_id"],
        data["prescription_date"],
        data["lab_test_required"]
    )

    return jsonify({
        "message": "Prescription created successfully",
        "prescription_id": prescription_id
    }), 201

#PUT
@prescription_bp.route("/prescriptions/<int:prescription_id>", methods=["PUT"])
def edit_prescription(prescription_id):

    data = request.get_json()

    required_fields = [
        "patient_id",
        "prescription_date",
        "lab_test_required"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "message": f"{field} is required"
            }), 400

    rows = update_prescription(
        prescription_id,
        data["patient_id"],
        data["prescription_date"],
        data["lab_test_required"]
    )

    if rows == 0:
        return jsonify({
            "message": "Prescription not found"
        }), 404

    return jsonify({
        "message": "Prescription updated successfully"
    }), 200

#DELETE
@prescription_bp.route("/prescriptions/<int:prescription_id>", methods=["DELETE"])
def remove_prescription(prescription_id):

    rows = delete_prescription(prescription_id)

    if rows == 0:
        return jsonify({
            "message": "Prescription not found"
        }), 404

    return jsonify({
        "message": "Prescription deleted successfully"
    }), 200