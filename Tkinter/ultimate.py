import tkinter as tk

root = tk.Tk()
root.title("Ultimate Exercise")
root.config(bg = "lightgray")

# CONFIGURE THE ROW AND COLUMNS
root.grid_rowconfigure(0, weight = 1)
root.grid_rowconfigure(1, weight = 3)
root.grid_rowconfigure(2, weight = 1)
root.grid_rowconfigure(3, weight = 1)
root.grid_columnconfigure(0, weight = 3)
root.grid_columnconfigure(1, weight = 1)

# TITLE
my_title = tk.Label(text = "Finish it", fg = "blue", bg = "lightblue")
my_title.grid(row=0, column=0, sticky="nsew")

# LISTBOX
listbox = tk.Listbox(root, height = 3, selectmode = "single", bg = "lightblue")
scrollbar = tk.Scrollbar(root, orient = tk.VERTICAL, command = listbox.yview)
listbox.grid(row = 1, column = 0, sticky = "nsew")
scrollbar.grid(row = 1, column = 1, sticky = "nsw")
listbox.config(yscrollcommand = scrollbar.set)

# SELECTED SHOWCASE
selected = tk.StringVar(value = "Select an item")

# FUNCTION TO UPDATE SELECTED
def update_selected(event = None):
    try:
        selection = listbox.curselection()
        if selection:
            selected.set(listbox.get(selection))
        else:
            selected.set("No selection")
    except:
        selected.set("No selection")

# DISPLAY
showcase = tk.Label(root, textvariable = selected)
showcase.grid(row = 4, column = 0)
listbox.bind("<<ListboxSelect>>", update_selected)


def add_list():
    value = entryBox.get()
    if value:
        listbox.insert(tk.END, value)
        print(f"{value} has been inserted")
        entryBox.delete(0, tk.END)
    else:
        print("Empty value")

def remove():
    value = listbox.curselection()
    listbox.delete(value)

# ENTRY TO ADD
entryBox = tk.Entry(root, bg = "lightpink")
entryBox.grid(row = 3, column = 0, columnspan = 2)

# BUTTON ADD
add_button = tk.Button(root, text = "ADD", bg = "lightblue", command = add_list)
add_button.grid(row = 2, column = 1, sticky = "nsew")

delete_button = tk.Button(root, text = "DELETE", bg = "lightblue", command = remove)
delete_button.grid(row = 2, column = 0, sticky = "nsew")

root.mainloop()