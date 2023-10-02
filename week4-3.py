import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showinfo("경고", "할 일을 입력하세요.")

def delete_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        task_listbox.delete(index)
        tasks.pop(index)
    else:
        messagebox.showinfo("경고", "할 일을 선택하세요.")

window = tk.Tk() 

window.title("To-Do List")

task_entry = tk.Entry(window, width=30)
task_entry.pack()

add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack()

task_listbox = tk.Listbox(window, selectmode=tk.SINGLE, width=30, height=10)
task_listbox.pack()

delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack()

window.mainloop() 

