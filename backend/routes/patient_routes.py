from flask import Blueprint, jsonify
from services.patient_service import get_all_patients

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