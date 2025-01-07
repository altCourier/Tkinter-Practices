import tkinter as tk

root = tk.Tk()
root.title("Fruit")

def update_label(event = None):
    selected_fruit.set(fruitList.get(fruitList.curselection()))

selected_fruit = tk.StringVar()

# FRUITS
fruits = ["Apple", "Banana", "Cherry", "Date", "Grapes", "Kiwi", "Lemon", "Mango", "Orange", "Peach", "Pear"]

# FRUIT LIST
fruitList = tk.Listbox(root, bg = "lightpink", selectmode = "single", height = 4)
fruitList.grid(row = 0, column = 1, padx = 20, pady = 20)

for fruit in fruits:
    fruitList.insert(tk.END, fruit)

# SCROLLBAR MANAGEMENT
scrollbar = tk.Scrollbar(root, orient = tk.VERTICAL, command = fruitList.yview)
scrollbar.grid(row = 0, column = 2, ipady = 5)

fruitList.config(yscrollcommand = scrollbar.set)

# DISPLAY FRUIT
fruitLabel = tk.Label(root, textvariable = selected_fruit, bg = "lightpink")
fruitLabel.grid(row = 1, column = 0, padx = 5, pady = 10, columnspan = 2)

fruitList.bind("<<ListboxSelect>>", update_label)
root.mainloop()
