from database.db import get_connection

def get_all_dispenses():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            dispense_id,
            prescription_id,
            staff_id,
            dispense_date
        FROM dispenses
        ORDER BY dispense_id;
    """)

    dispenses = cur.fetchall()

    cur.close()
    conn.close()

    return dispenses


def get_dispense_by_id(dispense_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            dispense_id,
            prescription_id,
            staff_id,
            dispense_date
        FROM dispenses
        WHERE dispense_id = %s;
    """, (dispense_id,))

    dispense = cur.fetchone()

    cur.close()
    conn.close()

    return dispense


def add_dispense(
    prescription_id,
    staff_id,
    dispense_date
):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO dispenses
        (
            prescription_id,
            staff_id,
            dispense_date
        )
        VALUES
        (%s,%s,%s)
        RETURNING dispense_id;
    """,
    (
        prescription_id,
        staff_id,
        dispense_date
    ))

    dispense_id = cur.fetchone()[0]

    conn.commit()

    cur.close()
    conn.close()

    return dispense_id


def update_dispense(
    dispense_id,
    prescription_id,
    staff_id,
    dispense_date
):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE dispenses
        SET
            prescription_id = %s,
            staff_id = %s,
            dispense_date = %s
        WHERE dispense_id = %s;
    """,
    (
        prescription_id,
        staff_id,
        dispense_date,
        dispense_id

    ))

    updated_rows = cur.rowcount

    conn.commit()

    cur.close()
    conn.close()

    return updated_rows


def delete_dispense(dispense_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM dispenses
        WHERE dispense_id = %s;
    """, (dispense_id,))

    deleted_rows = cur.rowcount

    conn.commit()

    cur.close()
    conn.close()

    return deleted_rows
