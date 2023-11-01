import tkinter as tk

# Task class with a 'completed' attribute
class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

# Task List (Component 1)
class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def get_all_tasks(self):
        return self.tasks

# GUI (Component 2)
class TaskGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        self.label = tk.Label(root, text="Task Manager")
        self.label.pack()

        self.text_area = tk.Text(root)
        self.text_area.pack()

        self.add_button = tk.Button(root, text="Add Task")
        self.add_button.pack()

        self.remove_button = tk.Button(root, text="Remove Task")
        self.remove_button.pack()

        self.mark_completed_button = tk.Button(root, text="Mark Completed")
        self.mark_completed_button.pack()

# Task Manager (Component 3)
class TaskManager:
    def __init__(self, gui, task_list):
        self.gui = gui
        self.task_list = task_list

        self.gui.add_button.config(command=self.add_task)
        self.gui.remove_button.config(command=self.remove_task)
        self.gui.mark_completed_button.config(command=self.mark_task_as_completed)

    def add_task(self):
        task = Task("New Task: ")  # In practice, you'd get this from the GUI input field
        self.task_list.add_task(task)
        self.update_task_list()

    def remove_task(self):
        if self.task_list.get_all_tasks():
            task = self.task_list.get_all_tasks()[0]  # Check if tasks exist before removal
            self.task_list.remove_task(task)
            self.update_task_list()

    def mark_task_as_completed(self):
        if self.task_list.get_all_tasks():
            task = self.task_list.get_all_tasks()[0]  # Check if tasks exist before marking as completed
            task.completed = True
            self.update_task_list()

    def update_task_list(self):
        tasks = self.task_list.get_all_tasks()
        self.gui.text_area.delete("1.0", "end")
        for task in tasks:
            self.gui.text_area.insert("end", f"{'[X] ' if task.completed else '[ ] '}{task.description}\n")

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    task_list = TaskList()
    gui = TaskGUI(root)
    manager = TaskManager(gui, task_list)

    # Initialize the task list with some tasks for testing
    task_list.add_task(Task("Task 1"))
    task_list.add_task(Task("Task 2"))

    # Test Case 1: Add Task
    def test_add_task():
        initial_task_count = len(task_list.get_all_tasks())
        manager.add_task()  # Adding a task
        updated_task_count = len(task_list.get_all_tasks())
        assert updated_task_count == initial_task_count + 1

    # Test Case 2: Remove Task
    def test_remove_task():
        initial_task_count = len(task_list.get_all_tasks())
        manager.remove_task()  # Removing a task
        updated_task_count = len(task_list.get_all_tasks())
        assert updated_task_count == initial_task_count - 1

    # Test Case 3: Mark Task as Completed
    def test_mark_task_as_completed():
        task_list.add_task(Task("Task 3"))
        manager.mark_task_as_completed()  # Marking a task as completed
        task = task_list.get_all_tasks()[0]
        updated_completed_status = task.completed
        assert updated_completed_status is True

    test_add_task()
    test_remove_task()
    test_mark_task_as_completed()

    root.mainloop()

