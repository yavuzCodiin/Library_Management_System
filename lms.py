import time

class Book:

    # Constructor => Initializes a new object of the Book class with title, author, release year, and number of pages.
    def __init__(self, book_name, author, release_year, numb_of_pages):
        self.book_name = book_name 
        self.author = author
        self.release_year = release_year
        self.numb_of_pages = numb_of_pages

    # Returns a string representation of the Book object to use print(book) in listing. 
    def __str__(self):
        return "\ntitle: {}\nauthor: {}\n".format(self.book_name, self.author) #print book names and authors only


class Library:

  # Constructor => Initializes a new object of the Library class
    def __init__(self):
        self.file = open('books.txt', 'a+', encoding='UTF-8') # Opens the 'books.txt' file in append+ mode, which allows reading, writing, appending.

    def load(self):
        self.file.seek(0) # Move the cursor to the beginning of the file
        book_list = self.file.read().splitlines() # Reads the lines of the file, removes leading/trailing whitespace, and splits them into a list.
        return book_list #returns list of book entries from the file
    
    # Lists all books in the library by creating Book objects from the book entries and printing them.
    def list_book(self):
        books = [line.split(',') for line in self.load() if line.strip() and len(line.split(',')) == 4] # Removes spaces, tabs, newlines and checks if we have 4 element(name,author,year,page) 
        if not books: #if there are no books, print "no book in database"
            print("no book in database")
        else: #else print book details 
            for book_name, author, release_year, numb_of_pages in books:
                print(Book(book_name, author, release_year, numb_of_pages))
                

    def add_book(self,book): #Adds a new book to the library by writing its details to the 'books.txt' file.
        str_book = "{}, {}, {}, {}\n".format(book.book_name, book.author, book.release_year, book.numb_of_pages)
        self.file.write(str_book)

    def remove_book(self, book_name): # Remove book according to given book name
        books = self.load() # Load books from database
        updated_books = [book for book in books if book.split(',')[0].lower() != book_name.lower()]  # Check the title which will be removed
        self.file.seek(0) # Move the cursor to the beginning of the file to overwrite from the start
        self.file.truncate() # Erase the current contents of the file
        self.file.writelines(updated_books) #  Write the updated book entries back to the file

    # Destructor => Prints a quitting message and closes the 'books.txt' file.
    def __del__(self): 
        print("Quitting...") 
        time.sleep(2) # sleep for 2 second
        self.file.close() # Close the file

# The main function that runs the library management system.
def main():
    lib = Library() # Creates a new Library object.
    
    # LMS MENU.
    print(
        """

        ***MENU***
        1) List Books
        2) Add Book
        3) Remove Book
        4) Quit
        
        """
          )

    # Main Loop
    while True:
        choice = int(input("Enter your choice: ")) #User's choice
        
        #List all books
        if choice == 1:
            print("Listing the books...")
            time.sleep(2)
            lib.list_book()

        #Add new book
        elif choice == 2:
        
            book_name = input("Book's title: ")
            author = input("Book's author: ")
            release_year = input("Book's release year: ")
            numb_of_pages = input("Book's total pages: ")
            new_book = Book(book_name, author, release_year, numb_of_pages)
            lib.add_book(new_book)

        #Remove book
        elif choice == 3:
            book_name=input("Enter the book title you want to remove: ")
            del_book=input("Do you want to remove?(e.g Yes/No): ")

            if del_book=="Yes":
                print("Removing the book...")
                time.sleep(2)
                lib.remove_book(book_name)
            else:
                continue
        
        #Exit program
        elif choice == 4:
            break

        # Wrong choice
        else:
            print("Invalid choice")  
    

if __name__ == '__main__':
    main()
