from functions import connection


def create_tables():
    """
    Creates all necessary tables in the database.
    """
    return (
        create_author(),
        create_publisher(),
        create_book(),
        create_client(),
        create_order(),
    )


def create_book():
    conn = connection.connection()
    cursor = conn.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS book (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        book_title TEXT NOT NULL,
        isbn INTEGER NOT NULL,
        price REAL NOT NULL,
        stock INTEGER DEFAULT 0,
        publisher_id INTEGER NOT NULL,
        author_id INTEGER NOT NULL,
        FOREIGN KEY (author_id) REFERENCES author(author_id)
    )"""
    )

    conn.commit()
    conn.close()
    return "Table 'book' has been created."


def create_publisher():
    conn = connection.connection()
    cursor = conn.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS publisher (
        publisher_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        publisher_name TEXT NOT NULL,
        publisher_email_contact TEXT NOT NULL
    )"""
    )

    conn.commit()
    conn.close()
    return "Table 'publisher' has been created."


def create_client():
    conn = connection.connection()
    cursor = conn.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS client (
        client_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        client_name TEXT NOT NULL,
        client_phone TEXT,
        client_email TEXT NOT NULL
    )"""
    )
    conn.commit()
    conn.close()
    return "Table 'client' has been created."


def create_author():
    conn = connection.connection()
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS author (
        author_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        author_name TEXT NOT NULL
    )"""
    )

    conn.commit()
    conn.close()
    return "Table 'author' has been created."


def create_order():
    """
    Creates the 'order' table in the database if it does not already exist.
    """
    conn = connection.connection()
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        client_id INTEGER NOT NULL,
        order_date DATE NOT NULL,
        order_total_price REAL NOT NULL,
        foreign key (client_id) references client(client_id)
    )"""
    )

    conn.commit()
    conn.close()
    return "Table 'order' has been created."
