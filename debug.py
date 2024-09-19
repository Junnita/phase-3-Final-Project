import sqlite3
from cli import LibraryCLI

def main():
    # Establish a connection to the SQLite database (or create it if it doesn't exist).
    conn = sqlite3.connect('library.db')

    # Create an instance of LibraryCLI with the database connection.
    library_cli = LibraryCLI(conn)

    # Create the necessary tables in the database.
    library_cli.create_tables()

    # Add authors and publishers.
    library_cli.add_author("Author 1")
    library_cli.add_author("Author 2")
    library_cli.add_publisher("Publisher 1")
    library_cli.add_publisher("Publisher 2")

    # List authors and publishers.
    print("Authors:")
    library_cli.list_authors()

    print("\nPublishers:")
    library_cli.list_publishers()

    # Add books and assign authors/publishers to them.
    library_cli.add_book("Book 1", "123")
    library_cli.add_book("Book 2", "456")
    library_cli.assign_author_to_book(1, 1)  # Assign Author 1 to Book 1
    library_cli.assign_publisher_to_book(2, 2)  # Assign Publisher 2 to Book 2

    # List books with authors and publishers.
    print("\nBooks:")
    library_cli.list_books()

    # Close the database connection.
    library_cli.close_connection()

if __name__ == "__main__":
    main()