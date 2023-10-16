library = {}  # Dictionary to store book information

def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    library[title] = author
    print("Book added successfully!")

def remove_book():
    title = input("Enter the title of the book you want to remove: ")
    if title in library:
        del library[title]
        print("Book removed successfully!")
    else:
        print("Book not found!")

def display_books():
    if library:
    
        print("List of books:")
        for title, author in library.items():
            print(f"Title: {title}\tAuthor: {author}")
    else:
        print("No books in the library!")

def search_book():
    title = input("Enter the title of the book you want to search: ")
    if title in library:
        print(f"Book '{title}' found!")
        print(f"Author: {library[title]}")
    else:
        print("Book not found!")

# Main program loop
while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Display Books")
    print("4. Search Book")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_book()
    elif choice == "2":
        remove_book()
    elif choice == "3":
        display_books()
    elif choice == "4":
        search_book()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 5.")