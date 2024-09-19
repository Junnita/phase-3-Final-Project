import sqlite3
from cli import LibraryCLI

def main():
    # Establish a connection to the SQLite database (or create it if it doesn't exist).
    conn = sqlite3.connect('library.db')

    # Create an instance of LibraryCLI with the database connection.
    library_cli = LibraryCLI(conn)

    # Create the necessary tables in the database.
    library_cli.create_tables()

    # Function to handle user preferences
    def handle_preferences():
        while True:
            print("\nOptions:")
            print("🖊️ a. Add an Author")
            print("🏢 b. Add a Publisher")
            print("📚 c. Add a Book")
            print("👤 d. List of all Authors")
            print("📝 e. List of all Publishers")
            print("📖 f. List of all Books")
            print("✏️ g. Update an Author")
            print("🔄 h. Update a Publisher")
            print("🔧 i. Update a Book")
            print("❌ j. Delete an Author")
            print("🗑️ k. Delete a Publisher")
            print("🗑️ l. Delete a Book")
            print("🔍 m. Find Author by ID")
            print("🔎 n. Find Publisher by ID")
            print("📖 o. Find Book by ID")
            print("🚪 p. Quit")

            choice = input("Choose an option (a-p): ")

            if choice == 'a':
                author_name = input("Enter the author's name: ")
                library_cli.add_author(author_name)
                print(f"Author '{author_name}' added successfully! 🎉")

            elif choice == 'b':
                publisher_name = input("Enter the publisher's name: ")
                library_cli.add_publisher(publisher_name)
                print(f"Publisher '{publisher_name}' added successfully! 🎉")

            elif choice == 'c':
                book_title = input("Enter the book title: ")
                book_description = input("Enter the book description: ")
                book_id = library_cli.add_book(book_title, book_description)

                # Assign author and publisher
                author_id = int(input("Enter the author ID for this book: "))
                publisher_id = int(input("Enter the publisher ID for this book: "))
                library_cli.assign_author_to_book(author_id, book_id)
                library_cli.assign_publisher_to_book(publisher_id, book_id)

                print(f"Book '{book_title}' added successfully! 📖")

            elif choice == 'd':
                print("\nAuthors:")
                library_cli.list_authors()

            elif choice == 'e':
                print("\nPublishers:")
                library_cli.list_publishers()

            elif choice == 'f':
                print("\nBooks:")
                library_cli.list_books()

            elif choice == 'g':
                author_id = int(input("Enter the author ID to update: "))
                new_name = input("Enter the new name: ")
                library_cli.update_author(author_id, new_name)
                print("Author updated successfully! ✏️")

            elif choice == 'h':
                publisher_id = int(input("Enter the publisher ID to update: "))
                new_name = input("Enter the new name: ")
                library_cli.update_publisher(publisher_id, new_name)
                print("Publisher updated successfully! ✏️")

            elif choice == 'i':
                book_id = int(input("Enter the book ID to update: "))
                new_title = input("Enter the new title: ")
                new_description = input("Enter the new description: ")
                library_cli.update_book(book_id, new_title, new_description)
                print("Book updated successfully! ✏️")

            elif choice == 'j':
                author_id = int(input("Enter the author ID to delete: "))
                library_cli.delete_author(author_id)
                print("Author deleted successfully! ❌")

            elif choice == 'k':
                publisher_id = int(input("Enter the publisher ID to delete: "))
                library_cli.delete_publisher(publisher_id)
                print("Publisher deleted successfully! ❌")

            elif choice == 'l':
                book_id = int(input("Enter the book ID to delete: "))
                library_cli.delete_book(book_id)
                print("Book deleted successfully! ❌")

            elif choice == 'm':
                author_id = int(input("Enter the author ID to find: "))
                author = library_cli.find_author_by_id(author_id)
                if author:
                    print(f"Found Author: ID: {author[0]}, Name: {author[1]} ✅")
                else:
                    print("Author not found. ❌")

            elif choice == 'n':
                publisher_id = int(input("Enter the publisher ID to find: "))
                publisher = library_cli.find_publisher_by_id(publisher_id)
                if publisher:
                    print(f"Found Publisher: ID: {publisher[0]}, Name: {publisher[1]} ✅")
                else:
                    print("Publisher not found. ❌")

            elif choice == 'o':
                book_id = int(input("Enter the book ID to find: "))
                book = library_cli.find_book_by_id(book_id)
                if book:
                    print(f"Found Book: ID: {book[0]}, Title: {book[1]}, Description: {book[2]} ✅")
                else:
                    print("Book not found. ❌")

            elif choice == 'p':
                print("Goodbye!!! 😘")

                
                break

            else:
                print("Invalid choice, please try again. ❗")

    # Handle user preferences
    handle_preferences()

    # Close the database connection.
    library_cli.close_connection()

if __name__ == "__main__":
    main()
