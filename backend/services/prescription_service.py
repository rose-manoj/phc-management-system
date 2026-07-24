from database.db import get_connection

def get_all_prescriptions():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            prescription_id,
            patient_id,
            prescription_date,
            lab_test_required
        FROM prescription
        ORDER BY prescription_id;
    """)

    prescriptions = cur.fetchall()

    cur.close()
    conn.close()

    return prescriptions

#GET BY ID 
def get_prescription_by_id(prescription_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            prescription_id,
            patient_id,
            prescription_date,
            lab_test_required
        FROM prescription
        WHERE prescription_id = %s;
    """, (prescription_id,))

    prescription = cur.fetchone()

    cur.close()
    conn.close()

    return prescription

#INSERT
def add_prescription(patient_id, prescription_date, lab_test_required):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO prescription
        (
            patient_id,
            prescription_date,
            lab_test_required
        )
        VALUES
        (%s, %s, %s)
        RETURNING prescription_id;
    """,
    (
        patient_id,
        prescription_date,
        lab_test_required
    ))

    prescription_id = cur.fetchone()[0]

    conn.commit()

    cur.close()
    conn.close()

    return prescription_id

#UPDATE
def update_prescription(
    prescription_id,
    patient_id,
    prescription_date,
    lab_test_required
):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE prescription
        SET
            patient_id = %s,
            prescription_date = %s,
            lab_test_required = %s
        WHERE prescription_id = %s;
    """,
    (
        patient_id,
        prescription_date,
        lab_test_required,
        prescription_id
    ))

    updated_rows = cur.rowcount

    conn.commit()

    cur.close()
    conn.close()

    return updated_rows

#DELETE
def delete_prescription(prescription_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM prescription
        WHERE prescription_id = %s;
    """, (prescription_id,))

    deleted_rows = cur.rowcount

    conn.commit()

    cur.close()
    conn.close()

    return deleted_rows