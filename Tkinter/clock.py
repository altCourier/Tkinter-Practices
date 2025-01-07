import tkinter as tk
import datetime

class Clock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Clock")
        self.config(bg = "lightblue")

        self.clockLabel = tk.Label(self, text = "Time is running...", bg = "lightblue")
        self.clockLabel.pack()

        self.timeVar = tk.StringVar()
        self.timeVar.set(self.get_current())

        self.timeEntry = tk.Entry(self, state = "readonly", textvariable = self.timeVar, bg = "mintcream")
        self.timeEntry.pack()

        self.update_time()

        self.mainloop()

    def get_current(self):
        return datetime.datetime.now().strftime("%H:%M:%S")

    def update_time(self):
        self.timeVar.set(self.get_current())
        self.after(1000, self.update_time)

if __name__ == "__main__":
    clock = Clock()