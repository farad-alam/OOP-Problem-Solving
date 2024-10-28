class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
        print(self.__book_created())

    def __book_created(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {self.available}"
    
    def update_availability(self, available_status):
        self.available = available_status
    
    


class Library:
    # __borrowed_books = {
    #     # member_id : [book1, book2, book3]

    # }

    def __init__(self, name):
        self.name = name
        self.__books = []
        self.__borrowed_books = {}


    def add_book(self, book):
        self.__books.append(book)
        print(f"{book.title} has been added to the {self.name}")
        return True

    def remove_book(self, book):
        self.__books.remove(book)
        print(f"{book.title} has been removed from the library")
        return True
    
    def book_list(self):
        print(f"Book List of {self.name}:")
        for book in self.__books:
            print(f"{book.title} - Available: {book.available}")

    # def check_availability(self, book):
    #     if book in self.__books:
    #         print(f"{book.title} is available")
    #     else:
    #         print(f"{book.title} is not available") 
    
    
    def borrow_book(self, member, book):
        if book in self.__books and book.available:
            if member.id not in self.__borrowed_books:
                self.__borrowed_books[member.id] = [book]
                book.update_availability(False)
                print(f"{book.title} has been borrowed by {member.name}")
            else:
                self.__borrowed_books[member.id].append(book)
                book.update_availability(False)
                print(f"{book.title} has been borrowed by {member.name}")
        else:
            print(f"{book.title} is not available to borrow")
            return False
    
    def return_book(self, member, book):
        if book in self.__borrowed_books[member.id]:
            self.__borrowed_books[member.id].remove(book)
            book.update_availability(True)
            print(f"{book.title} has been returned by {member.name}")
            return True
        else:
            print(f"{book.title} is not borrowed by {member.name}")
            return False


    def borrowed_books_details(self):
        for member_id, books in self.__borrowed_books.items():
            print(f"Borrowed books by {member_id}:")
            print(f"{member_id}: {', '.join(book.title for book in books)}")
    
    def borrowed_book_by_member(self, member):
        if member.id in self.__borrowed_books:
            for book in self.__borrowed_books[member.id]:
                print(f"Borroew book by {member.name}:")
                print(f"{book.title} by {book.author}")
    


class Member:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        print(self.__welcome())
    
    def __welcome(self):
        return f"Hi, {self.name}. You Account successfully created"


b1 = Book("The Alchemist", "Paulo Coelho", 123456, True)
b2 = Book("The Subtle Art of Not Giving a F*ck", "Mark Manson", 234567, True)
l1 = Library("Green Library")
l1.add_book(b1)
# l1.add_book(b2)
l1.book_list()
# l1.check_availability(b1)

m1 = Member("Farad Alam", 1234)

l2 = Library("Tech Library")
l2.add_book(b2)
l2.book_list()
