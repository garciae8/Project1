import tkinter as tk
import time

# Function to perform bubble sort and update the GUI
def bubble_sort_gui(rectangles, canvas):
    n = len(rectangles)
    for i in range(n):
        for j in range(0, n-i-1):
            # Highlight rectangles being compared
            rectangles[j].config(bg='yellow')
            rectangles[j+1].config(bg='yellow')
            canvas.update()
            time.sleep(0.2)  # Adjust speed as needed

            if rectangles[j].height > rectangles[j+1].height:
                # Swap heights
                rectangles[j].height, rectangles[j+1].height = rectangles[j+1].height, rectangles[j].height
                # Update rectangle colors after swapping
                rectangles[j].config(bg='green')
                rectangles[j+1].config(bg='green')
                canvas.update()
                time.sleep(0.2)  # Adjust speed as needed
            else:
                # No swap, reset colors
                rectangles[j].config(bg='red')
                rectangles[j+1].config(bg='red')
                canvas.update()
                time.sleep(0.2)  # Adjust speed as needed

            # Reset colors after comparison
            rectangles[j].config(bg='white')
            rectangles[j+1].config(bg='white')

# Function to create rectangles in the GUI
def create_rectangles(canvas, nums):
    rectangles = []
    width = 30
    margin = 10

    for i, num in enumerate(nums):
        height = num * 10
        x = i * (width + margin)
        rect = canvas.create_rectangle(x, 0, x + width, height, fill='white')
        rect.height = height
        rectangles.append(rect)

    return rectangles

# Function to start the sorting process
def start_sort(rectangles, canvas):
    bubble_sort_gui(rectangles, canvas)

# GUI setup
def create_gui(nums):
    root = tk.Tk()
    root.title("Sorting Visualization")

    canvas = tk.Canvas(root, width=len(nums) * 40, height=max(nums) * 10 + 20)
    canvas.pack()

    rectangles = create_rectangles(canvas, nums)

    sort_button = tk.Button(root, text="Sort", command=lambda: start_sort(rectangles, canvas))
    sort_button.pack()

    root.mainloop()

# Test the GUI
nums = [4, 2, 7, 1, 9, 5, 3, 8, 6, 0]
create_gui(nums)

