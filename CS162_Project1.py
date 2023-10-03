class Book:
    """ This simulates a book cretor 
    
        Contents that make a book are: Title of book, Name of the auther of the book,
        Genre of the book, Number of pages of the book

        One result for this book simulator can be: 
        Book name: The Beljar, 
        Author Name: Sylvia Plath ,
        Genre: Novel , 
        Page number: 210
    """
    def __init__(self):
        self.title = ""
        self.author = ""
        self.genre = ""
        self.pages = 0

    def read(self):
        print(f"You are now reading '{self.title}' by {self.author}.")

    def describe(self):
        print(f"Book Info:\nTitle: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}")
        print(f"Number of Pages: {self.pages}")

def main():
    print("Book Reader")
    book = Book()

    #Test Case 1: Create and Describe a Book
    
    book.title = "Test Book 1"
    book.author = "Test Author 1"
    book.genre = "Test Genre 1"
    book.pages = 100

    #Test Case 2: Read a Book

    book.title = "Test Book 2"
    book.author = "Test Author 2"
    book.genre = "Test Genre 2"
    book.pages = 200

    while True:
        print("\nMenu:")
        print("1. Create a Book")
        print("2. Read the Book")
        print("3. Describe the Book")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book.title = input("Enter book title: ")
            book.author = input("Enter book author: ")
            book.genre = input("Enter book genre: ")
            book.pages = int(input("Enter number of pages: "))
        elif choice == "2":
            book.read()
        elif choice == "3":
            book.describe()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
