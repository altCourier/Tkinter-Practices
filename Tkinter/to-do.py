import tkinter as tk

root = tk.Tk()
root.title("To-Do List")
root.config(bg = "lightpink")

def add_to_list():
    value = taskEntry.get()
    if value:
        taskList.insert(tk.END, value)
        taskEntry.delete(0, tk.END)

def remove_from_list():
    values = taskList.curselection()
    for value in reversed(values):
        taskList.delete(value)


start_title = tk.Label(root, text = "To-Do List App")
start_title.grid(row = 0, column = 0, columnspan = 2)

taskEntry = tk.Entry(root)
taskEntry.grid(row = 1, column = 0)

addButton = tk.Button(root, text = "ADD", command = add_to_list)
addButton.grid(row = 2, column = 0)

removeButton= tk.Button(root, text = "REMOVE", command = remove_from_list)
removeButton.grid(row = 3, column = 0)

taskList = tk.Listbox(root, selectmode = "multiple")
taskList.grid(row = 1, column = 1, rowspan = 4, sticky = "nswe")

scrollbar = tk.Scrollbar(root, orient = tk.VERTICAL, command = taskList.yview)
scrollbar.grid(row = 1, column = 2, rowspan = 4, sticky = "nsw")

taskList.config(yscrollcommand = scrollbar.set)
root.mainloop()
