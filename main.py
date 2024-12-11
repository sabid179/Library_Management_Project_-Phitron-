"""
Author      : Md. Rakibul Islam Sabid
Date        : 11-dec-2024
Description : Library Management System [-Phitron Assignment-]
"""


class Library:
    book_list = []
    
    
    def __init__(self):
        pass
    
    
    @classmethod
    def entry_book(self, book):
        self.book_list.append(book)
        
        
class Book:
    def __init__(self, book_id, title, author, availability):
        self.__book_id = book_id            # private attribute
        self._title = title                 # protected attribute
        self._author = author               # protected attribute
        self._availability = availability   # protected attribute
        
        Library.entry_book(self)
    
    
    @property
    def book_id(self):
        return self.__book_id;
    
    
    @property
    def availability(self):
        return self._availability;
        
        
    def borrow_book(self):
        if self._availability == True:
            self._availability = False
        print("You borrowed a Book..!")
            
            
    def return_book(self):
        self._availability = True
        print("You returned a Book..!")
        
    
    def view_book_info(self):
        output = f"Book ID: {self.__book_id}\nTitle: {self._title}\nAuthor: {self._author}\nAvailability: {self._availability}"""
        
        print(output)


# Adding some example book
# Available book id's: 101, 102, 103, 104, 105
for _ in range(5):
    my_book = Book((_ + 1) + 100, "Book_" + str(_ + 1), "Author_" + str(_ + 1), True)
        
        
while (True):
    prompt = """\n\n1. View All Book\n2. Borrow Book\n3. Return Book\n4. Exit\n\nEnter your choice: """
    
    print(prompt, end='')

    user_command = int(input())
    
    if user_command == 1:
        if len(Library.book_list) == 0:
           print("No Book Available!")
        else:
            print('\n')
             
        for book in Library.book_list:
            book.view_book_info()
            print()
            
    elif user_command == 2:
        borrow_book_id = int(input("Enter book ID: "))
        is_book_id_valid = False
        
        for book in Library.book_list:
            if book.book_id == borrow_book_id:
                is_book_id_valid = True
                
                if book.availability == True:
                    book.borrow_book()
                    
                else:
                    print('This Book is not available for borrowing..')
                
        if not is_book_id_valid:
            print('Invalid Book ID!')
                
    elif user_command == 3:
        return_book_id = int(input("Enter book ID: "))
        is_book_id_valid = False
        
        for book in Library.book_list:
            if book.book_id == return_book_id:
                is_book_id_valid = True
                
                if book.availability == False:
                    book.return_book()
                    
                else:
                    print('This Book was not even borrowed..')
                
        if not is_book_id_valid:
            print('Invalid Book ID!')
                
    else:
        print('Exiting...')
        break