from database.db import get_connection


def get_all_medicines():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            medicine_id,
            prescription_id,
            medicine_name,
            dosage,
            quantity
        FROM dispensed_medicines
        ORDER BY medicine_id;
    """)

    medicines = cur.fetchall()

    cur.close()
    conn.close()

    return medicines


def get_medicine_by_id(medicine_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            medicine_id,
            prescription_id,
            medicine_name,
            dosage,
            quantity
        FROM dispensed_medicines
        WHERE medicine_id = %s;
    """, (medicine_id,))

    medicine = cur.fetchone()

    cur.close()
    conn.close()

    return medicine


def add_medicine(
    prescription_id,
    medicine_name,
    dosage,
    quantity
):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO dispensed_medicines
        (
            prescription_id,
            medicine_name,
            dosage,
            quantity
        )
        VALUES
        (%s,%s,%s,%s)
        RETURNING medicine_id;
    """,
    (
        prescription_id,
        medicine_name,
        dosage,
        quantity
    ))

    medicine_id = cur.fetchone()[0]

    conn.commit()

    cur.close()
    conn.close()

    return medicine_id


def update_medicine(
    medicine_id,
    prescription_id,
    medicine_name,
    dosage,
    quantity
):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE dispensed_medicines
        SET
            prescription_id = %s,
            medicine_name = %s,
            dosage = %s,
            quantity = %s
        WHERE medicine_id = %s;
    """,
    (
        prescription_id,
        medicine_name,
        dosage,
        quantity,
        medicine_id
    ))

    updated_rows = cur.rowcount

    conn.commit()

    cur.close()
    conn.close()

    return updated_rows


def delete_medicine(medicine_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM dispensed_medicines
        WHERE medicine_id = %s;
    """, (medicine_id,))

    deleted_rows = cur.rowcount

    conn.commit()

    cur.close()
    conn.close()

    return deleted_rows