import tkinter # Grouped under the tkinter name.
# Need to use the prefix tkinter

root = tkinter.Tk()
root.title("Fridge")

my_Text = "Yurtta sulh, cihanda sulh"
magnet = tkinter.Label(root, text=my_Text)
magnet.pack()

root.mainloop()