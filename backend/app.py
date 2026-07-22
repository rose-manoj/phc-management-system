from flask import Flask
from database.db import get_connection

app = Flask(__name__)


@app.route("/")
def home():

    try:
        conn = get_connection()
        conn.close()
        return "Database Connected Successfully!"

    except Exception as e:
        return f"Connection Failed: {e}"


if __name__ == "__main__":
    app.run(debug=True)