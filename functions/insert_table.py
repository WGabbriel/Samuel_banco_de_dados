import pandas as pd
import functions.connection as connection


def insert():
    """
    Inserts data into the tables.
    """
    insert_author()
    insert_publisher()
    insert_book()
    insert_client()
    insert_order()
    return "Dados inseridos com sucesso"


def insert_publisher():
    conn = connection.connection()
    pd.DataFrame(
        {
            "publisher_id": [1, 2, 3],
            "publisher_name": ["Penguin", "Harper Collins", "Random House"],
            "publisher_email_contact": [
                "penguin@email.com",
                "harpercollins@email.com",
                "randomhouse@gmail.com",
            ],
        }
    ).to_sql("publisher", conn, if_exists="replace", index=False)
    conn.close()
    return "Data has been inserted into the publisher table."


def insert_book():
    conn = connection.connection()
    pd.DataFrame(
        {
            "book_id": [1, 2, 3],
            "book_title": [
                "The Great Gatsby",
                "The Catcher in the Rye",
                "To Kill a Mockingbird",
            ],
            "isbn": [123456789, 987654321, 123789456],
            "price": [10.99, 9.99, 8.99],
            "stock": [100, 100, 100],
            "publisher_id": [1, 2, 3],
            "author_id": [1, 2, 3],
        }
    ).to_sql("book", conn, if_exists="replace", index=False)
    conn.close()
    return "Data has been inserted into the book table."


def insert_client():
    conn = connection.connection()
    pd.DataFrame(
        {
            "client_id": [1, 2, 3],
            "client_name": ["John Doe", "Jane Doe", "Alice Smith"],
            "client_phone": ["123-456-7890", "987-654-3210", "123-789-4560"],
            "client_email": [
                "jonhdoe@email",
                "janedoe@email",
                "alicesmith@email",
            ],
        }
    ).to_sql("client", conn, if_exists="replace", index=False)
    conn.close()
    return "Data has been inserted into the client table."


def insert_author():
    conn = connection.connection()
    pd.DataFrame(
        {
            "author_id": [1, 2, 3],
            "author_name": [
                "F. Scott Fitzgerald",
                "J.D. Salinger",
                "Harper Lee",
            ],
        }
    ).to_sql("author", conn, if_exists="replace", index=False)
    conn.close()
    return "Data has been inserted into the author table."


def insert_order():
    conn = connection.connection()
    pd.DataFrame(
        {
            "order_id": [1, 2, 3],
            "client_id": [1, 2, 3],
            "book_id": [1, 2, 3],
            "order_date": ["2021-01-01", "2021-01-02", "2021-01-03"],
            "quantity": [1, 2, 3],
        }
    ).to_sql("orders", conn, if_exists="replace", index=False)
    conn.close()
    return "Data has been inserted into the orders table."
