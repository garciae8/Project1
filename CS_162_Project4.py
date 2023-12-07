import tkinter as tk  # Import the tkinter library and alias it as tk
import pytest  # Import the pytest library

# GUI code
class MyApp:
    def __init__(self):
        # Create a Tkinter root window
        self.root = tk.Tk()
        # Set the title of the root window
        self.root.title("Smallest Number Finder")

        # Create a list to store Entry widgets
        self.text_boxes = []
        # Create 10 Entry widgets and add them to the list
        for i in range(10):
            text_box = tk.Entry(self.root)
            text_box.pack()  # Pack the Entry widget into the root window
            self.text_boxes.append(text_box)

        # Create a "Find Smallest" button with a command to call the find_smallest method
        self.find_button = tk.Button(self.root, text="Find Smallest", command=self.find_smallest)
        self.find_button.pack()  # Pack the button into the root window

        # Create a "Next Smallest" button with a command to call the next_smallest method
        self.next_button = tk.Button(self.root, text="Next Smallest", command=self.next_smallest)
        self.next_button.pack()  # Pack the button into the root window

        # Create a Label widget to display the smallest number
        self.label = tk.Label(self.root, text="")
        self.label.pack()  # Pack the label into the root window

        # Initialize a list to store numbers entered in the Entry widgets
        self.numbers = []

    def find_smallest(self):
        """Find the smallest number in the list of entry boxes in this GUI and puts the result into self.label."""
        # Get the content of each Entry widget and convert it to a list of numbers
        numbers_strings = [box.get() for box in self.text_boxes]
        self.numbers = []
        # Convert each string to a float and handle ValueErrors
        for current_string in numbers_strings:
            try:
                self.numbers.append(float(current_string))
            except ValueError:
                print(f"A ValueError has occurred: {current_string} is not a number.")

        # Find the smallest number, update the label, and remove it from the list
        smallest = min(self.numbers)
        self.label.config(text=str(smallest))
        self.numbers.remove(smallest)

    def next_smallest(self):
        """Find the next smallest number in the list, remove that number from the list, and puts that smallest number in the label."""
        # Check if there are numbers left in the list
        if self.numbers:
            # Find the smallest number, update the label, and remove it from the list
            smallest = min(self.numbers)
            self.label.config(text=str(smallest))
            self.numbers.remove(smallest)
        else:
            # If no numbers are left, update the label with a message
            self.label.config(text="No numbers left to check.")

# PyTests
# Define a fixture for the GUI
@pytest.fixture
def app():
    # Create an instance of the MyApp class and return its root window as the fixture
    app = MyApp().root
    yield app  # Yield the app for testing
    app.destroy()  # Destroy the app after testing

# Test that the label displays the smallest number
def test_find_smallest(app):
    app.update()
    app.geometry("300x200")

    # Insert values into Entry widgets
    app.children["!entry"].insert(0, "5.0")
    app.children["!entry2"].insert(0, "3.0")
    app.children["!entry3"].insert(0, "7.0")

    # Trigger the "Find Smallest" button
    app.children["!button"].invoke()
    # Assert that the label text matches the expected value
    assert app.children["!label"].cget("text") == "3.0"

# Test that the "Next Smallest" button works
def test_next_smallest(app):
    app.update()
    app.geometry("300x200")

    # Insert values into Entry widgets
    app.children["!entry"].insert(0, "5.0")
    app.children["!entry2"].insert(0, "3.0")
    app.children["!entry3"].insert(0, "7.0")

    # Trigger the "Find Smallest" button and then the "Next Smallest" button
    app.children["!button"].invoke()
    app.children["!button2"].invoke()
    # Assert that the label text matches the expected value
    assert app.children["!label"].cget("text") == "5.0"

if __name__ == "__main__":
    # Run the tests using pytest
    pytest.main()
