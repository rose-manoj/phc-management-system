from database.db import get_connection


def get_all_treatments():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            treatment_id,
            patient_id,
            staff_id,
            visit_date,
            remarks
        FROM treats
        ORDER BY treatment_id;
    """)

    treatments = cur.fetchall()

    cur.close()
    conn.close()

    return treatments


def get_treatment_by_id(treatment_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            treatment_id,
            patient_id,
            staff_id,
            visit_date,
            remarks
        FROM treats
        WHERE treatment_id = %s;
    """, (treatment_id,))

    treatment = cur.fetchone()

    cur.close()
    conn.close()

    return treatment


def add_treatment(patient_id, staff_id, visit_date, remarks):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO treats
        (
            patient_id,
            staff_id,
            visit_date,
            remarks
        )
        VALUES
        (%s, %s, %s, %s)
        RETURNING treatment_id;
    """,
    (
        patient_id,
        staff_id,
        visit_date,
        remarks
    ))

    treatment_id = cur.fetchone()[0]

    conn.commit()

    cur.close()
    conn.close()

    return treatment_id


def update_treatment(
    treatment_id,
    patient_id,
    staff_id,
    visit_date,
    remarks
):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE treats
        SET
            patient_id = %s,
            staff_id = %s,
            visit_date = %s,
            remarks = %s
        WHERE treatment_id = %s;
    """,
    (
        patient_id,
        staff_id,
        visit_date,
        remarks,
        treatment_id
    ))

    updated_rows = cur.rowcount

    conn.commit()

    cur.close()
    conn.close()

    return updated_rows


def delete_treatment(treatment_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM treats
        WHERE treatment_id = %s;
    """, (treatment_id,))

    deleted_rows = cur.rowcount

    conn.commit()

    cur.close()
    conn.close()

    return deleted_rows