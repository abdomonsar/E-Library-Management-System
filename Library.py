class Library:
    def __init__(self):
        self.books={}
        self.users={}
        self.max_limit=3
    def add_book(self,book):
        self.books[book.isbn] =book
        print(f"Book '{book.title}' added to the library.")
    def add_user(self,user):
        self.users[user.user_id]=user   
        print(f"User '{user.name}' registered successfully.")
    def borrow_book(self, user_id, isbn):
        if user_id not in self.users:
            print("Error: User not found!")
            return
        if isbn not in self.books:
            print("Error: Book not found!")
            return     
        user = self.users[user_id]
        book = self.books[isbn]
        if not book.is_available:
            print(f"Error: '{book.title}' is already borrowed.")
        elif len(user.borrowed_books) >= self.max_limit:
            print(f"Error: {user.name} has reached the maximum limit ({self.max_limit} books).")
        else:
            # 3. تنفيذ عملية الاستعارة
            book.is_available = False
            book.borrower_id = user_id
            user.borrowed_books.append(isbn)
            print(f"Success: {user.name} borrowed '{book.title}'.")
            
    def return_book(self, user_id, isbn):
        # 1. التحقق من وجود المستخدم والكتاب في النظام
         if user_id in self.users and isbn in self.books:
            user = self.users[user_id]
            book = self.books[isbn]

            if isbn in user.borrowed_books:
                 
                book.is_available = True
                book.borrower_id = None
                user.borrowed_books.remove(isbn)  
                user.history.append(book.title)  
                
                print(f"Success: {user.name} returned '{book.title}'.")

                rate = int(input(f"How would you rate '{book.title}' from 1 to 5? "))
                if 1 <= rate <= 5:
                    book.rating.append(rate)
                    print("Thank you for your rating!")
            else:
                print(f"Error: {user.name} does not have this book.")
         else:
            print("Error: Invalid User ID or ISBN.")
    def search_books(self, search_term, search_type):
         
        results = []
        term = search_term.lower() # تحويل نص البحث لصغير لضمان دقة النتائج

        for book in self.books.values():
            if search_type == "1" and term in book.title.lower():
                results.append(book)
            elif search_type == "2" and term in book.author.lower():
                results.append(book)
            elif search_type == "3" and term in book.category.lower():
                results.append(book)

         
        if results:
            print(f"\n--- Found {len(results)} Books ---")
            for book in results:
                print(book)
        else:
            print(f"\nNo books found matching '{search_term}'.")
        
        