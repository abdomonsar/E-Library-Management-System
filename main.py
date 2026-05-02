from book import Book
from user import User
from Library import Library

def main():
    my_library = Library()

    while True:
        print("\n" + "="*30)
        print(" LIBRARY MANAGEMENT SYSTEM ")
        print("="*30)
        print("1. Add New Book")
        print("2. Register New User")
        print("3. Search for a Book")
        print("4. Borrow a Book")
        print("5. Return a Book")
        print("6. Show Library Statistics")
        print("7. Exit")
        
        choice = input("\nChoose an option (1-7): ")

        if choice == "1":
            isbn = input("Enter ISBN: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            cat = input("Enter Category: ")
            year = input("Enter Year: ")
            pages = input("Enter Pages: ")
            new_book = Book(isbn, title, author, cat, year, pages)
            my_library.add_book(new_book)

        elif choice == "2":
            uid = input("Enter User ID: ")
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            new_user = User(uid, name, email)
            my_library.add_user(new_user)

        elif choice == "3":
            print("\nSearch by: 1.Title | 2.Author | 3.Category")
            s_type = input("Choice: ")
            term = input("Enter search keyword: ")
            my_library.search_books(term, s_type)

        elif choice == "4":
            uid = input("Enter User ID: ")
            isbn = input("Enter Book ISBN: ")
            my_library.borrow_book(uid, isbn)

        elif choice == "5":
            uid = input("Enter User ID: ")
            isbn = input("Enter Book ISBN: ")
            my_library.return_book(uid, isbn)

        elif choice == "6":
            print(f"\nTotal Books: {len(my_library.books)}")
            print(f"Total Users: {len(my_library.users)}")

        elif choice == "7":
            print("Closing the Library System... Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

main() 
 