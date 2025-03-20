from functions.drop_table import drop
from functions.insert_table import insert
from functions.delete_database import delete_database
from functions.join_tables import left_join, inner_join
from functions.create_table import create_tables
from functions.select_table import select_table


if __name__ == "__main__":

    print("\nDeleting database:")
    print(delete_database())

    print("\nCreating tables:")
    print(create_tables())

    print("\nInserting into tables:")
    print(insert())

    print("\nSelecting from tables:")
    print(select_table("book"))

    print("\nPerforming left join:")
    print(left_join("book", "author", "author_id"))

    print("\nPerforming inner join:")
    print(inner_join("book", "author", "author_id"))

    print("Dropping tables:")
    print(drop("book"))
