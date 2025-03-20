import pandas as pd
import functions.connection as connection


def select_table(table_name):
    conn = connection.connection()
    select_query = f"""
    SELECT *
    FROM {table_name};
    """
    select_result = pd.read_sql(select_query, conn)
    conn.close()
    return select_result
