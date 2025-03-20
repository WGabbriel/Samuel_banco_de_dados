import sqlite3


def connection():
    conn = sqlite3.connect("database.db")
    return conn
