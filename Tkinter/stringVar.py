import tkinter as tk

root = tk.Tk()
root.title("StringVar Example")

text_var = tk.StringVar()

entry = tk.Entry(root, textvariable = text_var)
entry.pack()

def print_text():
    print(f"{text_var.get()} has been entered.")

button = tk.Button(root, text = "Print it.", command = print_text)
button.pack()

label = tk.Label(root, textvariable = text_var)
label.pack()

text_var.set("Hello, Lumen.")

root.mainloop()