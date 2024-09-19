import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist).
conn = sqlite3.connect('library.db')
c = conn.cursor()

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

# Commit changes and close the connection.
conn.commit()
conn.close()