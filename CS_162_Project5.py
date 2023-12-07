import tkinter as tk
import time

class SearchGUI:
    def __init__(self, master, data):
        # Initialize the SearchGUI class with a master window and data.
        self.master = master
        self.data = data
        self.current_index = 0

        # Create a canvas in the master window with dimensions 400x200.
        self.canvas = tk.Canvas(master, width=400, height=200)
        self.canvas.pack()

        # Create an entry widget for text input in the master window.
        self.text_entry = tk.Entry(master)
        self.text_entry.pack()

        # Create a scale widget for selecting search speed in the master window.
        self.speed_scale = tk.Scale(master, from_=1, to=10, orient=tk.HORIZONTAL, label="Search Speed")
        self.speed_scale.set(5)
        self.speed_scale.pack()

        # Create a button for initiating the search in the master window.
        self.search_button = tk.Button(master, text="Search", command=self.start_search)
        self.search_button.pack()

    def start_search(self):
        # Get the target value and search speed from the entry and scale widgets.
        target_value = int(self.text_entry.get())
        speed = self.speed_scale.get()
        # Call the search method with the target value and search speed.
        self.search(target_value, speed)

    def search(self, target, speed):
        # Iterate through the data and highlight bars based on the search progress.
        for i, value in enumerate(self.data):
            self.highlight_bar(i, "yellow")

            if value == target:
                # Highlight the bar in green if the target value is found.
                self.highlight_bar(i, "green")
                # Schedule a function to reset colors after 1000 milliseconds (1 second).
                self.master.after(1000, lambda: self.reset_colors())
                # Print a message indicating the target value and its index.
                print(f"Value {target} found at index {i}")
                return
            else:
                # Highlight the bar in red if the current value is not the target.
                self.highlight_bar(i, "red")
                # Update the master window and pause execution based on the search speed.
                self.master.update()
                time.sleep(speed / 10.0)
                # Schedule a function to reset colors immediately after updating the window.
                self.master.after(0, lambda: self.reset_colors())

        # Print a message indicating that the target value was not found in the dataset.
        print(f"Value {target} not found in the dataset")

    def highlight_bar(self, index, color):
        # Highlight a bar on the canvas based on the index and color.
        x0, y0, x1, y1 = index * 4, 0, (index + 1) * 4, self.data[index] * 2
        self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)

    def reset_colors(self):
        # Clear all items on the canvas and reset bar colors to white.
        self.canvas.delete("all")
        for i, value in enumerate(self.data):
            self.highlight_bar(i, "white")

# Example usage:
# Define a dataset and create a Tkinter root window.
data = [5, 8, 3, 1, 9, 4, 6, 7, 2, 0, 10, 15, 12, 11, 14, 13]
root = tk.Tk()
# Create an instance of the SearchGUI class with the root window and dataset.
app = SearchGUI(root, data)
# Start the Tkinter event loop.
root.mainloop()