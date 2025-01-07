import tkinter as tk

root = tk.Tk()

# Create the Listbox widget
taskList = tk.Listbox(root)
taskList.grid(row=1, column=1, rowspan=2, sticky="nsew", padx=5, pady=5)  # sticky="nsew" allows Listbox to expand

# Create the Scrollbar widget and link it to the Listbox
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=taskList.yview)
scrollbar.grid(row=1, column=2, rowspan=2, sticky="ns", padx=5, pady=5)  # sticky="ns" makes scrollbar expand vertically

# Configure Listbox to use the scrollbar
taskList.config(yscrollcommand=scrollbar.set)

root.mainloop()
