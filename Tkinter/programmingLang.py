import tkinter as tk

root = tk.Tk()
root.title("Programming Languages Listbox")
root.geometry("300x300")


listbox = tk.Listbox(root, selectmode = "multiple", height = 10)
listbox.pack()

languages = ["Python", "Java", "C++", "JavaScript", "Ruby"]
for lang in languages:
    listbox.insert(tk.END, lang)

def add_language():
    new_lang = entry.get()
    if new_lang:
        listbox.insert(tk.END, new_lang)
        entry.delete(0, tk.END)

def delete_languages():
    selected_indices = listbox.curselection()
    for i in selected_indices:
        listbox.delete(i)

def print_selected():
    selected_indices = listbox.curselection()
    selected_items = [listbox.get(i) for i in selected_indices]
    print("Selected Languages:", selected_items)

entry = tk.Entry(root)
entry.pack()

btn_add = tk.Button(root, text = "Add Lang.", command = add_language)
btn_add.pack()

btn_delete = tk.Button(root, text="Delete Selected", command=delete_languages)
btn_delete.pack(pady=5)

btn_print = tk.Button(root, text="Print Selected", command=print_selected)
btn_print.pack(pady=5)

root.mainloop()