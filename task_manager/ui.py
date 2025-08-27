import tkinter as tk
from tkinter import messagebox
import commands
from functools import partial

def handle_delete(id, app):
    commands.delete_task(id)
    show_all_tasks_frame(app)


# This function is responsible for submition
def submit_task(title, app):
    if not title:
        messagebox.showerror(
            title="Add Task",
            message="Can not add empty task",
            parent=app
        )
    else:
        commands.save_task({"title": title})
        show_all_tasks_frame(app)

# This function is responsible for showing the all tasks frame
def show_add_task_frame(app):
    frame = tk.Frame(master=app)
    frame.grid(row=0, column=0, sticky="NSEW", padx=10, pady=10)

    label = tk.Label(master=frame, text="What do you wanna do? ")
    label.grid()
    entry = tk.Entry(master=frame)
    entry.grid()

    btn = tk.Button(
        master=frame,
        text="Submit",
        command=lambda: submit_task(entry.get(), app))
    btn.grid()
    frame.tkraise()

def show_all_tasks_frame(app):
    frame = tk.Frame(master=app)
    frame.grid(row=0, column=0, sticky="NSEW", padx=10, pady=10)

    tasks = commands.get_tasks().to_list()
    for task in tasks:
        checkbtn = tk.Checkbutton(master=frame, text=task["title"])
        checkbtn.grid(row=tasks.index(task), column=0)
        
        edit_btn = tk.Button(master=frame, text="Edit")
        edit_btn.grid(row=tasks.index(task), column=1) # .index(task); finds the index of each tasks and puts it as the row

        deletebtn =tk.Button(
            master=frame,
            text="Delete",
            command=partial(handle_delete, task["_id"], app)) # First use of partial.. 
        deletebtn.grid(row=tasks.index(task), column=2)
        # updatebtn =tk.Button(master=frame, text="Update")
        # updatebtn.grid(row=tasks.index(task), column=2)

    btn = tk.Button(master=frame, text="Add Task", command=lambda: show_add_task_frame(app)) # Give this a command that would take you to the add task frame
    btn.grid(row=len(tasks)+1, column=0)

    frame.tkraise()