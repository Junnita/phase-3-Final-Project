# LIBRARY MANAGEMENT SYSTEM 
Library Management System allows you to create tables , add authors,
publishers, and books, assign authors and publishers to books, and perform various other operations on the library database.

## Features

- Create tables for authors, publishers, books, book authors, and book publishers.
- Add authors, publishers, and books to the database.
- Assign authors and publishers to books.
- List all authors, publishers, and books.
- Update author, publisher, and book details.
- Find authors, publishers, and books by their IDs.
- Close the database connection.
- You can also delete any author , publishers or books

## Installation

### Alternative One

1. Clone the repository:
    ```sh
    git clone https://github.com/Junnita/phase-3-Final-Project.git
    ```
2. Navigate to the project directory:
    ```sh
    cd phase-3-Final-Project
    ```
3. Install the required dependencies (if any).



### Alternative Two
- On the top right corner of this page there is a button labelled Fork.

- Click on Fork to create a copy of the repository to your github account.

- Follow the process described in Alternative One above.



## Usage

1. Import the `sqlite3` module and create a connection to the database:
    ```python
    import sqlite3
    from library_cli import LibraryCLI

    conn = sqlite3.connect('library.db')
    cli = LibraryCLI(conn)
    ```

2. Create the necessary tables:
    ```python
    cli.create_tables()
    ```

3. Add authors, publishers, and books:
    ```python
    cli.add_author('Author Name')
    cli.add_publisher('Publisher Name')
    book_id = cli.add_book('Book Title', 'Book Description')
    ```

4. Assign authors and publishers to books:
    ```python
    cli.assign_author_to_book(author_id, book_id)
    cli.assign_publisher_to_book(publisher_id, book_id)
    ```

5. List all authors, publishers, and books:
    ```python
    cli.list_authors()
    cli.list_publishers()
    cli.list_books()
    ```

6. Update author, publisher, and book details:
    ```python
    cli.update_author(author_id, 'New Author Name')
    cli.update_publisher(publisher_id, 'New Publisher Name')
    cli.update_book(book_id, 'New Book Title', 'New Book Description')
    ```

7. Find authors, publishers, and books by their IDs:
    ```python
    author = cli.find_author_by_id(author_id)
    publisher = cli.find_publisher_by_id(publisher_id)
    book = cli.find_book_by_id(book_id)
    ```

8. Close the database connection:
    ```python
    cli.close_connection()
    ```


### Author 
- JUNNE WANJA ❤️
