class Book:
    def __init__(self,title,author,isbn,category,year,pages):
         self.title=title
         self.author=author
         self.isbn=isbn,
         self.category=category
         self.year=year
         self.pages=pages
         self.is_available=True
         self.borrower_id = None  
         self.rating = [] 
         #Average book rating
    def get_average_rating(self):
           if not self.rating:
            return "No ratings yet"
           return sum(self.rating) / len(self.rating)     
    def __str__(self):
         status = "Available" if self.is_available else "Borrowed"
         avg_rate = self.get_average_rating()
         return (f"ISBN: {self.isbn} | {self.title}\n"
                f"Author: {self.author} | Category: {self.category}\n"
                f"Year: {self.year} | Pages: {self.pages}\n"
                f"Rating: {avg_rate} | Status: {status}\n"
                f"{'-'*40}")
     
     
         