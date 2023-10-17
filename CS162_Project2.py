class Book:
    """ This simulates a book creator with attributes like Title, Author, Genre, and Pages. """

    def __init__(self):
        self.title = ""
        self.author = ""
        self.genre = ""
        self.pages = 0

    def read(self):
        """ Simulate reading the book. """
        print(f"You are now reading '{self.title}' by {self.author}.")

    def describe(self):
        """ Describe the book's attributes. """
        print(f"Book Info:\nTitle: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}")
        print(f"Number of Pages: {self.pages}")

def test_book_creation():
    """ Test creating a book object and setting its attributes. """
    book = Book()
    book.title = "Test Book 1"
    book.author = "Test Author 1"
    book.genre = "Test Genre 1"
    book.pages = 100

    assert book.title == "Test Book 1"
    assert book.author == "Test Author 1"
    assert book.genre == "Test Genre 1"
    assert book.pages == 100

def test_read_book():
    """ Test the read() method. """
    book = Book()
    book.title = "Test Book 2"
    book.author = "Test Author 2"

    print("Expected Output: You are now reading 'Test Book 2' by Test Author 2.")
    print("Actual Output:")
    book.read()

def test_describe_book():
    """ Test the describe() method. """
    book = Book()
    book.title = "Test Book 3"
    book.author = "Test Author 3"
    book.genre = "Test Genre 3"
    book.pages = 150

    print("Expected Output:")
    print("Book Info:\nTitle: Test Book 3\nAuthor: Test Author 3\nGenre: Test Genre 3\nNumber of Pages: 150")
    print("Actual Output:")
    book.describe()

if __name__ == "__main__":
    # Run the test functions
    test_book_creation()
    test_read_book()
    test_describe_book()
