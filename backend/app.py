from flask import Flask
from routes.patient_routes import patient_bp
from routes.staff_routes import staff_bp
from routes.prescription_routes import prescription_bp
from routes.lab_test_routes import lab_test_bp
from routes.dispensed_medicines_routes import medicine_bp

app = Flask(__name__)

app.register_blueprint(patient_bp)
app.register_blueprint(staff_bp)
app.register_blueprint(prescription_bp)
app.register_blueprint(lab_test_bp)
app.register_blueprint(medicine_bp)

if __name__ == "__main__":
    app.run(debug=True)