from flask import Flask
from routes.patient_routes import patient_bp

app = Flask(__name__)

app.register_blueprint(patient_bp)

if __name__ == "__main__":
    app.run(debug=True)