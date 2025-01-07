import tkinter as tk

root = tk.Tk()
root.title("Fridge.")
root.geometry("300x300+100+100") # (100,100)
root.resizable(True, True)
root.minsize(300, 100)
root.maxsize(500, 500)
root.iconbitmap("logo.png")

root.config(bg = "pink")
root.alpha = 0.1

magnet = tk.Label(root, text = "Hey!")
magnet.pack()

root.mainloop()