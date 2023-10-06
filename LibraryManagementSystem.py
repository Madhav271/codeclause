# Initialize an empty library
library = {}

# Function to add a book to the library
def add_book():
    book_id = input("Enter book ID: ")
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    library[book_id] = {"title": title, "author": author}
    print(f"Book '{title}' by {author} added to the library.")

# Function to search for a book by title or author
def search_book():
    search_term = input("Enter book title or author to search: ")
    found_books = []
    
    for book_id, book_info in library.items():
        if search_term.lower() in book_info["title"].lower() or search_term.lower() in book_info["author"].lower():
            found_books.append((book_id, book_info))
    
    if found_books:
        print("Found books:")
        for book_id, book_info in found_books:
            print(f"Book ID: {book_id}")
            print(f"Title: {book_info['title']}")
            print(f"Author: {book_info['author']}")
    else:
        print("No books found with the given search term.")

# Function to display all books in the library
def display_books():
    if library:
        print("Books in the library:")
        for book_id, book_info in library.items():
            print(f"Book ID: {book_id}")
            print(f"Title: {book_info['title']}")
            print(f"Author: {book_info['author']}")
    else:
        print("The library is empty.")

# Main menu
while True:
    print("\nLibrary Management System")
    print("1. Add a book")
    print("2. Search for a book")
    print("3. Display all books")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        display_books()
    elif choice == "4":
        print("Thank you for using the Library Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
