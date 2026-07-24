from database.db import get_connection


def get_all_lab_tests():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            test_id,
            prescription_id,
            test_type,
            test_date,
            status,
            result
        FROM lab_test
        ORDER BY test_id;
    """)

    tests = cur.fetchall()

    cur.close()
    conn.close()

    return tests


def get_lab_test_by_id(test_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            test_id,
            prescription_id,
            test_type,
            test_date,
            status,
            result
        FROM lab_test
        WHERE test_id = %s;
    """, (test_id,))

    test = cur.fetchone()

    cur.close()
    conn.close()

    return test


def add_lab_test(
    prescription_id,
    test_type,
    test_date,
    status,
    result
):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO lab_test
        (
            prescription_id,
            test_type,
            test_date,
            status,
            result
        )
        VALUES
        (%s,%s,%s,%s,%s)
        RETURNING test_id;
    """,
    (
        prescription_id,
        test_type,
        test_date,
        status,
        result
    ))

    test_id = cur.fetchone()[0]

    conn.commit()

    cur.close()
    conn.close()

    return test_id


def update_lab_test(
    test_id,
    prescription_id,
    test_type,
    test_date,
    status,
    result
):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE lab_test
        SET
            prescription_id = %s,
            test_type = %s,
            test_date = %s,
            status = %s,
            result = %s
        WHERE test_id = %s;
    """,
    (
        prescription_id,
        test_type,
        test_date,
        status,
        result,
        test_id
    ))

    updated_rows = cur.rowcount

    conn.commit()

    cur.close()
    conn.close()

    return updated_rows


def delete_lab_test(test_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM lab_test
        WHERE test_id = %s;
    """, (test_id,))

    deleted_rows = cur.rowcount

    conn.commit()

    cur.close()
    conn.close()

    return deleted_rows