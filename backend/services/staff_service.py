from database.db import get_connection
def get_all_staff():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT
           staff_id,
           name,
           contact,
           dob,
           doj,
           role
        FROM staff
        ORDER BY staff_id;
    """)
    staff = cur.fetchall()
    cur.close()
    conn.close()
    return staff

def get_staff_by_id(staff_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT
            staff_id,
            name,
            contact,
            dob,
            doj,
            role
            FROM staff
            WHERE staff_id = %s;
    """, (staff_id,))

    staff = cur.fetchone()
    cur.close()
    conn.close()
    return staff

def add_staff(name, contact, dob, doj, role):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO  staff
        (
            name,
            contact,
            dob,
            doj,
            role
        )
        VALUES
        (%s, %s, %s, %s, %s)
        RETURNING staff_id;
    """,
    (
        name,
        contact,
        dob,
        doj,
        role
    ))

    staff_id = cur.fetchone()[0]

    conn.commit()

    cur.close()
    conn.close()

    return staff_id

def update_staff(staff_id, name, contact, dob, doj, role):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE staff
        SET
            name = %s,
            contact = %s,
            dob = %s,
            doj = %s,
            role = %s
        WHERE staff_id = %s;
    """,
    (
        name,
        contact,
        dob,
        doj,
        role,
        staff_id
    ))

    updated_rows = cur.rowcount

    conn.commit()

    cur.close()
    conn.close()

    return updated_rows

def delete_staff(staff_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM staff
        WHERE staff_id = %s;
    """, (staff_id,))

    deleted_rows = cur.rowcount

    conn.commit()

    cur.close()
    conn.close()

    return deleted_rows