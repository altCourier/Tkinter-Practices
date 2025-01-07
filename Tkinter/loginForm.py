import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Please login")
root.config(bg = "lightslategray")
root.bind("<Escape>", lambda x: quit())

root.grid_rowconfigure(0, weight = 4)
root.grid_rowconfigure(1, weight = 1)
root.grid_rowconfigure(2, weight = 1)

def login():
    if passwordEntry.get() == "1234" and userEntry.get() == "admin":
        messagebox.showinfo("Hey!", "Successful Login!")
    else:
        messagebox.showwarning("Failure!", "Try again!")
        print(f"{passwordEntry.get()} has been entered.")
        print(f"{userEntry.get()} has been entered.")

welcome = tk.Label(root, text = "Welcome, Please Login.", bg = "dimgray")
welcome.grid(row = 0, column = 0, columnspan = 2, sticky = "nsew", padx = 5, pady = 5)

userLabel = tk.Label(root, text = "Username", bg = "light blue")
userLabel.grid(row = 1, column = 0, sticky = "nsew", padx = 10, pady = 10)

passwordLabel = tk.Label(root, text = "Password", bg = "light blue")
passwordLabel.grid(row = 2, column = 0, sticky = "nsew", padx = 10, pady = 10)

userEntry = tk.Entry(root, fg = "gray")
userEntry.grid(row = 1, column = 1, sticky = "nsew", padx = 10, pady = 10)

passwordEntry = tk.Entry(root, fg = "gray", show = "*")
passwordEntry.grid(row = 2, column = 1, sticky = "nsew", padx = 10, pady = 10)

loginbutton = tk.Button(root, text = "Login", bg = "dimgray", command = login)
loginbutton.bind("<Return>", lambda x: login())
loginbutton.grid(row = 3, column = 0, columnspan = 2)

root.mainloop()