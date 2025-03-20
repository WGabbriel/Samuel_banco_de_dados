import os


def delete_database():
    os.remove("database.db")
    print("Database deleted successfully.")
    return
