# Harder challenge (stretch goal): 
# 
    # Create a Book class and BookShelf class that can be used to manage a collection of books. 
    # Create a Book class that has the following attributes: title (str), author (str), publisher (str), publication year (int). 
    # The class should also have a str method that returns the book's information in a formatted string. 
    # Create a BookShelf class that has the following attributes: 
    # capacity (int), list of books (list). 
    # The class should have the following methods: 
    # - add_book: adds a book to the list of books if the shelf is not full 
    # - remove_book: removes a book from the list of books if it exists on the shelf 
    # - find_book_by_title: searches for a book by its title and returns the book object if found 
    # - find_books_by_author: searches for books by a specific author and returns a list of book objects if found 
    # The class should also have a str method that returns a string representation of the books on the shelf. 
    # 
    # Create four Book objects and add them to a BookShelf object with a capacity of three. 
    # Test the BookShelf object by adding, removing, and finding books by title and author.
    # Print the BookShelf object after each action.

class Book:
    def __init__(self, title, author, publication_year ):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Published: {self.publication_year}"


#class Bookshelf(Book):
    #def __init__(self, title, author, publication_year, capacity, book_list):
    #    super().__init__(title, author, publication_year)
    #    self.capacity = capacity
    #    self.book_list = book_list  

class Bookshelf:
    def __init__(self, capacity):
        self.capacity = capacity
        self.books = []

    def add_a_book(self, book):
        if len(self.books) < self.capacity:
            self.books.append(book)
            print(f"{book} added the shelf.")
        else: print(f"The bookshelf is full. {book} cannot be added.")

    def remove_a_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"{book.title} has been removed from the bookshelf.")
        else:
            print(f"{book.title} by {book.author} is not on the bookshelf.")

    def find_a_book_by_title(self, title):
        for book in self.books:
            if book.title == book: 
                return book
        return None
        #if book in self.books:
        #    print(f"{book.title} was written by {book.author} and first published in {book.publication_year}. It is on teh bookshelf." )
        #else:
        #    print(f"{book.title} was written by {book.author} and first published in {book.publication_year}. It os not on the bookshelf.")

    def find_a_book_by_author(self):
        pass

    def __str__(self):
        bookshelf_content = [str(book) for book in self.books]
        #return super().__str__() + 
        return "\nBookshelf contents:\n" + "\n".join(bookshelf_content) 
    

book_1 = Book("The Lord of the Rings","Tolkien",1955)
book_2 = Book("Catch 22","Heller",1960)
book_3 = Book("The Beach","Garland",1996)
book_4 = Book("Perfume","Suskind",2002)

bookshelf = Bookshelf(3)

bookshelf.add_a_book(book_1)
bookshelf.add_a_book(book_2)
bookshelf.add_a_book(book_3)
bookshelf.add_a_book(book_4) # does not fit

print("")
print(bookshelf)
print("")
bookshelf.remove_a_book(book_2)
print("")
print(bookshelf)
print("")
bookshelf.add_a_book(book_4)
print(bookshelf)
print("")
bookshelf.remove_a_book(book_4)
print(bookshelf)
print("")