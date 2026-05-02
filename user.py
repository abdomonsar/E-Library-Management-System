class User:
    def __init__(self,user_id,name,email):
        self.user_id=user_id
        self.name=name
        self.email=email
        self.borrowed_books=[]
        self.history=[]
        self.fine = 0.0   
    def __str__(self):
        return (f"User ID: {self.user_id} | Name: {self.name}\n"
                f"Email: {self.email}\n"
                f"Currently Borrowing: {len(self.borrowed_books)} books\n"
                f"Total Fines: ${self.fine}\n"
                f"{'-'*30}")    