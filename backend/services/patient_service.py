from database.db import get_connection
def get_all_patients():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT
           patient_id,
           name,
           dob,
           gender,
           contact,
           health_status
        FROM patient
        ORDER BY patient_id;
    """)
    patients = cur.fetchall()
    cur.close()
    conn.close()
    return patients