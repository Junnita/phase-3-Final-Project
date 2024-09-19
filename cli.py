import sqlite3

class LibraryCLI:
    def __init__(self, conn):
        self.conn = conn

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
        c = self.conn.cursor()
        c.execute("INSERT INTO authors (name) VALUES (?)", (name,))
        self.conn.commit()
        print(f"Author '{name}' added successfully.")

    def list_authors(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM authors")
        authors = c.fetchall()
        if authors:
            for author in authors:
                print(f"ID: {author[0]}, Name: {author[1]}")
        else:
            print("No authors found.")    
    
    def add_publisher(self, name):
        c = self.conn.cursor()
        c.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
        self.conn.commit()
        print(f"Publisher '{name}' added successfully.")


    def list_publishers(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM publishers")
        publishers = c.fetchall()
        if publishers:
            for publisher in publishers:
                print(f"ID: {publisher[0]}, Name: {publisher[1]}")
        else:
            print("No publishers found.")


    def add_book(self, title, copy_number):
        c = self.conn.cursor()
        c.execute("INSERT INTO books (title, copy_number) VALUES (?, ?)", (title, copy_number))
        self.conn.commit()
        print(f"Book '{title}' added successfully.")


    def list_books(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM books")
        books = c.fetchall()
        if books:
            for book in books:
                print(f"ID: {book[0]}, Title: {book[1]}, Copy Number: {book[2]}, Available: {book[3]}, Author ID: {book[4]}, Publisher ID: {book[5]}")
        else:
            print("No books found.")


    def assign_author_to_book(self, book_id, author_id):
        c = self.conn.cursor()
        c.execute("UPDATE books SET author_id=? WHERE id=?", (author_id, book_id))
        self.conn.commit()
        print(f"Author ID '{author_id}' assigned to book ID '{book_id}' successfully.")

    def assign_publisher_to_book(self, book_id, publisher_id):
        c = self.conn.cursor()
        c.execute("UPDATE books SET publisher_id=? WHERE id=?", (publisher_id, book_id))
        self.conn.commit()
        print(f"Publisher ID '{publisher_id}' assigned to book ID '{book_id}' successfully.")

    def close_connection(self):
        self.conn.close()
        print("Connection closed.")