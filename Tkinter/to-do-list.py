import tkinter as tk

root = tk.Tk()
root.title("To-Do List")

def addtoList():
    value = entryBox.get()
    if value:
        taskList.insert(0, value)
        print(f"{value} has been inserted.")
        entryBox.delete(0, tk.END)
    else:
        print("Empty input")

def removefrom():
    values = [x for x in taskList.curselection()]
    for value in reversed(values):
        taskList.delete(value)
        print(f"Reomed task at index {value}")
    
# TITLE LABEL
titleLabel = tk.Label(root, text = "To-Do List")
titleLabel.grid(row = 0, column = 0, columnspan = 2)

# ADD LABEL
addButton = tk.Button(root, text = "ADD", bg = "pink", command = addtoList)
addButton.grid(row = 2, column = 0, padx = 10, pady = 10,)

# DELETE LABEL
deleteButton = tk.Button(root, text = "DELETE", bg = "pink", command = removefrom)
deleteButton.grid(row = 1, column = 0, padx = 10, pady = 10,)

# ENTRY BOX
entryBox = tk.Entry(root, bg = "light pink")
entryBox.grid(row = 3, column = 0, padx = 10, pady = 10, columnspan = 2)

# LISTBOX
taskList = tk.Listbox(root, bg = "light pink", selectmode = "multiple")
taskList.grid(row = 1, column = 1, rowspan = 2, sticky = "nsew")

scrollbar = tk.Scrollbar(root, orient = tk.VERTICAL, command = taskList.yview)
scrollbar.grid(row = 1, column = 2, rowspan = 2, sticky = "ns")

taskList.config(yscrollcommand = scrollbar.set)


root.mainloop()