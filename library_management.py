# Library Management System
# Beginner Python Project

library = []

def add_book():
    book_name = input("Enter book name: ")
    library.append(book_name)
    print("Book added successfully!")

def view_books():
    if not library:
        print("No books available.")
    else:
        print("\nBooks in Library:")
        for book in library:
            print("-", book)

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice. Try again.")

main()
