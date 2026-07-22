from flask import Blueprint, jsonify, request
from services.patient_service import get_all_patients, add_patient

patient_bp = Blueprint("patients", __name__)


@patient_bp.route("/patients", methods=["GET"])
def get_patients():

    patients = get_all_patients()

    patient_list = []

    for patient in patients:

        patient_list.append({

            "patient_id": patient[0],
            "name": patient[1],
            "dob": patient[2],
            "gender": patient[3],
            "contact": patient[4],
            "health_status": patient[5]

        })

    return jsonify(patient_list)


from services.patient_service import get_patient_by_id


@patient_bp.route("/patients/<int:patient_id>", methods=["GET"])
def fetch_patient(patient_id):

    patient = get_patient_by_id(patient_id)

    if patient is None:
        return jsonify({"message": "Patient not found"}), 404

    patient_data = {

        "patient_id": patient[0],
        "name": patient[1],
        "dob": patient[2],
        "gender": patient[3],
        "contact": patient[4],
        "health_status": patient[5]

    }

    return jsonify(patient_data), 200

@patient_bp.route("/patients", methods=["POST"])
def create_patient():

    data = request.get_json()

    required_fields = [
        "name",
        "dob",
        "gender"
    ]

    for field in required_fields:

        if field not in data:

            return jsonify({
                "message": f"{field} is required"
            }), 400

    patient_id = add_patient(

        data["name"],
        data["dob"],
        data["gender"],
        data.get("contact"),
        data.get("health_status")

    )

    return jsonify({

        "message": "Patient created successfully",

        "patient_id": patient_id

    }), 201