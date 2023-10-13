"""
Author: Salem BenMna
Date written: 10/12/23
Assignment: M08 Final Project
Short Desc: This GUI program allows users to manage different tasks in multiple categories using Tkinter library.
"""

import tkinter as tk
from tkinter import ttk
import re

# Function to update the task listbox based on selected category
def showTasks():
    """
    Update the task listbox based on the selected category.
    """
    category = categoryVar.get()
    taskListbox.delete(0, tk.END) 
    for task, is_done in tasks.get(category, []):
        status = "Done" if is_done else "Not Done"
        taskListbox.insert(tk.END, f"{task} - {status}")

# Function to add a new task
def addTask():
    """
    Add a new task to the selected category.
    """
    category = categoryVar.get() #categoryVar: A StringVar() instance to hold the currently selected category in the dropdown menu.
    task = taskEntry.get() #taskEntry: An Entry widget where the user can input a new task.

    # data validation
    if task.strip() == '' or not re.match("^[A-Za-z\s]+$", task):
        # Show error message if task is empty or contains invalid characters
        error_window = tk.Toplevel(root) #error_window: Toplevel() instance used to create additional windows for error messages.
        error_window.title("Error")  
        error_window.geometry("200x100")

        error_label = tk.Label(error_window, text="Please enter a valid task", font=("Arial", 12)) #error_label: Label widgets used to display text in the error window.
        error_label.pack(padx=10, pady=10)
        return

    tasks.setdefault(category, []).append((task, False))
    showTasks()

# Function to toggle the status of a task
def toggleTask():
    """
    Toggle the status of the selected task.
    """
    selected_task = taskListbox.curselection()
    if selected_task:
        index = selected_task[0] #index: An index representing the currently selected task in the listbox.
        task, is_done = tasks[categoryVar.get()][index]
        tasks[categoryVar.get()][index] = (task, not is_done)
        showTasks()

# Function to delete a task
def deleteTask():
    """
    Delete the selected task.
    """
    selected_task = taskListbox.curselection()
    if selected_task:
        index = selected_task[0]
        tasks[categoryVar.get()].pop(index)
        showTasks()

# Function to open a window showing task details
def openDetailsWindow(task, is_done):
    """
    Open a window to display details of a selected task.
    """
    details_window = tk.Toplevel(root) #details_window: Toplevel() instance used to create additional windows for task details.
    details_window.title("Task Details")
    details_window.geometry("300x150")

    details_label = tk.Label(details_window, text=f"Task: {task}\nStatus: {'Done' if is_done else 'Not Done'}", font=("Arial", 12)) #details_label: Label widget used to display text in the details window.
    details_label.pack(padx=10, pady=10)

# Function to show details of a selected task
def showDetails():
    """
    Show details of the selected task.
    """
    selected_task = taskListbox.curselection()
    if selected_task:
        index = selected_task[0]
        task, is_done = tasks[categoryVar.get()][index]
        openDetailsWindow(task, is_done)
    else:
        details_window = tk.Toplevel(root)
        details_window.title("Task Details")
        details_window.geometry("200x100")
        
        details_label = tk.Label(details_window, text="Please select a task", font=("Arial", 12))
        details_label.pack(padx=10, pady=10)

# Function to exit the application
def exitApp():
    """
    Exit the application.
    """
    root.destroy()

# Sample data structure to hold tasks
tasks = {
    "House": [("Clean the house", False), ("Do laundry", False)],
    "School": [("Finish homework", False), ("Study for exam", False)],
    "Gym": [("Curl Ups exercise", False)]
} #tasks: A dictionary that will hold the tasks organized by category.

# Create the main window
root = tk.Tk()
root.title("Task Manager Pro")

# Set window size
root.geometry("500x650")

# Load the background image
background_photo = tk.PhotoImage(file="background.png") #background_photo: PhotoImage instance representing the background image used for the GUI.

# Load the heart image
heart_photo = tk.PhotoImage(file="heart.png") #heart_photo: PhotoImage instance representing the heart image used for the GUI.

# Load the bulb image
bulb_photo = tk.PhotoImage(file="bulb.png") #bulb_photo: PhotoImage instance representing the bulb image used for the GUI.

# Create a label for the background image
background_label = tk.Label(root, image=background_photo) #background_label: Label widgets to display the background image.
background_label.place(relwidth=1, relheight=1) 

# Create a label for the heart image
heart_label = tk.Label(root, image=heart_photo) #heart_label: Label widgets to display the heart image.
heart_label.pack(side=tk.BOTTOM, pady=(0, 10))

# Create a label for the bulb image
bulb_label = tk.Label(root, image=bulb_photo) #bulb_label: Label widgets to display the bulb image.
bulb_label.pack(side=tk.BOTTOM, pady=(0, 10))

# Category dropdown
categoryVar = tk.StringVar(root)
categoryVar.set("House")
categoryDropdown = ttk.Combobox(root, values=["House", "School", "Gym"], textvariable=categoryVar, font=("Arial", 12), justify="center")  #categoryDropdown: A Combobox widget allowing the user to select a category.
categoryDropdown.pack(pady=(10, 0))

# Listbox to display tasks
taskListbox = tk.Listbox(root, font=("Arial", 12), selectbackground="#D9EDF7", selectforeground="black") #taskListbox: A Listbox widget that will display the list of tasks.
taskListbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)


# Button to show tasks
showTasksButton = tk.Button(root, text="Show Tasks", command=showTasks, font=("Arial", 12), bg="#5BC0DE", fg="white")
showTasksButton.pack(pady=(0, 10))

# Entry to add tasks
taskEntry = tk.Entry(root, font=("Arial", 12))
taskEntry.pack(pady=(0, 10), fill=tk.BOTH, expand=True)

# Button to add task
addTaskButton = tk.Button(root, text="Add Task", command=addTask, font=("Arial", 12), bg="#5CB85C", fg="white")
addTaskButton.pack()

# Button to toggle task
toggleTaskButton = tk.Button(root, text="Toggle Task", command=toggleTask, font=("Arial", 12), bg="#F0AD4E", fg="white")
toggleTaskButton.pack(pady=(10, 0))

# Button to delete task
deleteTaskButton = tk.Button(root, text="Delete Task", command=deleteTask, font=("Arial", 12), bg="#D9534F", fg="white")
deleteTaskButton.pack(pady=(0, 10))

# Button to view details
detailsButton = tk.Button(root, text="View Details", command=showDetails, font=("Arial", 12), bg="#D9534F", fg="white")
detailsButton.pack(pady=(0, 10))

# Button to exit the application
exitButton = tk.Button(root, text="Exit", command=exitApp, font=("Arial", 12), bg="#FF6347", fg="white")
exitButton.pack(pady=(0, 10)) #showTasksButton, addTaskButton, toggleTaskButton, deleteTaskButton, detailsButton, exitButton: Buttons for various actions.

# Start the main event loop
root.mainloop()