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

def get_patient_by_id(patient_id):
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
            WHERE patient_id = %s;
    """, (patient_id,))

    patients = cur.fetchone()
    cur.close()
    conn.close()
    return patients

def add_patient(name, dob, gender, contact, health_status):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO  patient
        (
            name,
            dob,
            gender,
            contact,
            health_status
        )
        VALUES
        (%s, %s, %s, %s, %s)
        RETURNING patient_id;
    """,
    (
        name,
        dob,
        gender,
        contact,
        health_status
    ))

    patient_id = cur.fetchone()[0]

    conn.commit()

    cur.close()
    conn.close()

    return patient_id

def update_patient(patient_id, name, dob, gender, contact, health_status):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE patient
        SET
            name = %s,
            dob = %s,
            gender = %s,
            contact = %s,
            health_status = %s
        WHERE patient_id = %s;
    """,
    (
        name,
        dob,
        gender,
        contact,
        health_status,
        patient_id
    ))

    updated_rows = cur.rowcount

    conn.commit()

    cur.close()
    conn.close()

    return updated_rows

def delete_patient(patient_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM patient
        WHERE patient_id = %s;
    """, (patient_id,))

    deleted_rows = cur.rowcount

    conn.commit()

    cur.close()
    conn.close()

    return deleted_rows