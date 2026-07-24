from flask import Blueprint, request, jsonify

from services.treats_service import (
    get_all_treatments,
    get_treatment_by_id,
    add_treatment,
    update_treatment,
    delete_treatment
)

treats_bp = Blueprint("treats", __name__)

#GET ALL
@treats_bp.route("/treatments", methods=["GET"])
def fetch_treatments():
    return jsonify(get_all_treatments())

#GET BY ID
@treats_bp.route("/treatments/<int:treatment_id>", methods=["GET"])
def fetch_treatment(treatment_id):

    treatment = get_treatment_by_id(treatment_id)

    if treatment is None:
        return jsonify({
            "message": "Treatment not found"
        }),404

    return jsonify(treatment)

#POST
@treats_bp.route("/treatments", methods=["POST"])
def create_treatment():

    data = request.get_json()

    required_fields = [
        "patient_id",
        "staff_id",
        "visit_date",
        "remarks"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "message": f"{field} is required"
            }),400

    treatment_id = add_treatment(
        data["patient_id"],
        data["staff_id"],
        data["visit_date"],
        data["remarks"]
    )

    return jsonify({
        "message":"Treatment created successfully",
        "treatment_id":treatment_id
    }),201

#PUT
@treats_bp.route("/treatments/<int:treatment_id>", methods=["PUT"])
def edit_treatment(treatment_id):

    data = request.get_json()

    required_fields = [
        "patient_id",
        "staff_id",
        "visit_date",
        "remarks"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "message": f"{field} is required"
            }),400

    rows = update_treatment(
        treatment_id,
        data["patient_id"],
        data["staff_id"],
        data["visit_date"],
        data["remarks"]
    )

    if rows == 0:
        return jsonify({
            "message":"Treatment not found"
        }),404

    return jsonify({
        "message":"Treatment updated successfully"
    })

#DELETE
@treats_bp.route("/treatments/<int:treatment_id>", methods=["DELETE"])
def remove_treatment(treatment_id):

    rows = delete_treatment(treatment_id)

    if rows == 0:
        return jsonify({
            "message":"Treatment not found"
        }),404

    return jsonify({
        "message":"Treatment deleted successfully"
    })