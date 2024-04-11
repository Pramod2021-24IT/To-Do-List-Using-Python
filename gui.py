import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Task Added Successfully")
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_name = task_listbox.get(selected_index)
        task_listbox.delete(selected_index)
        messagebox.showinfo("Success", f"Task '{task_name}' Removed Successfully")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def clear_tasks():
    task_listbox.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List Manager")

# Create frames
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

list_frame = tk.Frame(root)
list_frame.pack(padx=10, pady=(0, 10))

# Task entry
task_entry = tk.Entry(input_frame, width=50)
task_entry.grid(row=0, column=0, padx=(0, 5))

add_button = tk.Button(input_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, pady=(0, 10))

# Task list
task_listbox = tk.Listbox(list_frame, width=50, height=10)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

# Buttons
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(side=tk.LEFT, padx=(0, 5))

clear_button = tk.Button(root, text="Clear All", command=clear_tasks)
clear_button.pack(side=tk.LEFT)

root.mainloop()
