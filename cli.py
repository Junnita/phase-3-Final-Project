import sqlite3

class LibraryCLI:
    def __init__(self, connection):
        self.conn = connection

    def create_tables(self):
        c = self.conn.cursor()

        # Create the authors table.
        c.execute('''
            CREATE TABLE IF NOT EXISTS authors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')

        # Create the publishers table.
        c.execute('''
            CREATE TABLE IF NOT EXISTS publishers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')

        # Create the books table with foreign key relationships to authors and publishers.
        c.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                copy_number TEXT NOT NULL,
                available INTEGER DEFAULT 1,
                author_id INTEGER,
                publisher_id INTEGER,
                FOREIGN KEY(author_id) REFERENCES authors(id),
                FOREIGN KEY(publisher_id) REFERENCES publishers(id)
            )
        ''')

        self.conn.commit()
    def add_author(self, name):
        with self.conn:
            self.conn.execute("INSERT INTO authors (name) VALUES (?)", (name,))

    def add_publisher(self, name):
        with self.conn:
            self.conn.execute("INSERT INTO publishers (name) VALUES (?)", (name,))

    def add_book(self, title, description):
        with self.conn:
            self.conn.execute("INSERT INTO books (title, description) VALUES (?, ?)", (title, description))
            return self.conn.execute("SELECT last_insert_rowid()").fetchone()[0]

    def assign_author_to_book(self, author_id, book_id):
        with self.conn:
            self.conn.execute("INSERT INTO book_authors (book_id, author_id) VALUES (?, ?)", (book_id, author_id))

    def assign_publisher_to_book(self, publisher_id, book_id):
        with self.conn:
            self.conn.execute("INSERT INTO book_publishers (book_id, publisher_id) VALUES (?, ?)", (book_id, publisher_id))

    def list_authors(self):
        cursor = self.conn.execute("SELECT id, name FROM authors")
        for row in cursor:
            print(f"ID: {row[0]}, Name: {row[1]}")

    def list_publishers(self):
        cursor = self.conn.execute("SELECT id, name FROM publishers")
        for row in cursor:
            print(f"ID: {row[0]}, Name: {row[1]}")

    def list_books(self):
        cursor = self.conn.execute("SELECT id, title, description FROM books")
        for row in cursor:
            print(f"ID: {row[0]}, Title: {row[1]}, Description: {row[2]}")

    def update_author(self, author_id, new_name):
        with self.conn:
            self.conn.execute("UPDATE authors SET name = ? WHERE id = ?", (new_name, author_id))

    def update_publisher(self, publisher_id, new_name):
        with self.conn:
            self.conn.execute("UPDATE publishers SET name = ? WHERE id = ?", (new_name, publisher_id))

    def update_book(self, book_id, new_title, new_description):
        with self.conn:
            self.conn.execute("UPDATE books SET title = ?, description = ? WHERE id = ?", (new_title, new_description, book_id))

    def find_author_by_id(self, author_id):
        cursor = self.conn.execute("SELECT * FROM authors WHERE id = ?", (author_id,))
        return cursor.fetchone()

    def find_publisher_by_id(self, publisher_id):
        cursor = self.conn.execute("SELECT * FROM publishers WHERE id = ?", (publisher_id,))
        return cursor.fetchone()

    def find_book_by_id(self, book_id):
        cursor = self.conn.execute("SELECT * FROM books WHERE id = ?", (book_id,))
        return cursor.fetchone()

    # Delete methods
    def delete_author(self, author_id):
        with self.conn:
            self.conn.execute("DELETE FROM authors WHERE id = ?", (author_id,))

    def delete_publisher(self, publisher_id):
        with self.conn:
            self.conn.execute("DELETE FROM publishers WHERE id = ?", (publisher_id,))

    def delete_book(self, book_id):
        with self.conn:
            self.conn.execute("DELETE FROM books WHERE id = ?", (book_id,))

    def close_connection(self):
        self.conn.close()
