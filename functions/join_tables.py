import pandas as pd
import functions.connection as connection


def inner_join(table1, table2, join_column):
    conn = connection.connection()
    inner_query = f"""
    SELECT *
    FROM {table1}
    INNER JOIN {table2}
    ON {table1}.{join_column} = {table2}.{join_column};
    """
    inner_join_result = pd.read_sql_query(inner_query, conn)
    return inner_join_result


def left_join(table1, table2, join_column):
    conn = connection.connection()
    left_query = f"""
    SELECT *
    FROM {table1}
    LEFT JOIN {table2}
    ON {table1}.{join_column} = {table2}.{join_column};
    """
    left_join_result = pd.read_sql_query(left_query, conn)
    return left_join_result
