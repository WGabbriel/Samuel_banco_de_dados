import functions.connection as connection


def drop(table_name):
    """
    Drops the tables.
    """
    conn = connection.connection()
    cursor = conn.cursor()
    cursor.execute(f"DROP TABLE if exists {table_name}")
    conn.commit()
    conn.close()
    return f"Table {table_name} has been dropped."
