import tkinter as tk

root = tk.Tk()
root.title("Expense Tracker")
root.config(bg = "thistle")

def add_income():
    value = enterExpen.get()
    if "," in value:
        value = value.replace(",", ".")
    try:
        if float(value):
            income.insert(tk.END, value)
            enterExpen.delete(0, tk.END)
            calculate_result()
        else:
            print("Missing income input")

    except ValueError:
        print("Enter a numeric value.")
        enterExpen.delete(0, tk.END)

def add_outcome():
    value = enterExpen.get()
    if "," in value:
        value = value.replace(",", ".")
    try:
        if float(value):
            outcome.insert(tk.END, value)
            enterExpen.delete(0, tk.END)
            calculate_result()
        else:
            print("Missing outcome input")
    except ValueError:
        print("Enter a numeric input")
        enterExpen.delete(0, tk.END)

def calculate_result():
    incomes = income.get(0, tk.END)
    outcomes = outcome.get(0, tk.END)
    result = 0
    for inc in incomes:
        result += float(inc)

    for outc in outcomes:
        result -= float(outc)

    resultVar.set(result)

# TITLE LABEL
my_title = tk.Label(root, text = "Expense Tracker", bg = "thistle")
my_title.grid(row = 0, column = 0, columnspan = 6)

# INCOME LIST
income = tk.Listbox(root, bg = "lavenderblush")
income.grid(row = 1, column = 1, sticky = "nsew", rowspan = 6)

incomeScrollbar = tk.Scrollbar(root, orient = tk.VERTICAL, command = income.yview)
incomeScrollbar.grid(row = 1, column = 0, sticky = "nsew", rowspan = 6)

income.config(yscrollcommand = incomeScrollbar.set)

# OUTCOME LIST
outcome = tk.Listbox(root, bg = "lavenderblush")
outcome.grid(row = 1, column = 3, sticky = "nsew", rowspan = 6)

outcomeScrollbar = tk.Scrollbar(root, orient = tk.VERTICAL, command = outcome.yview)
outcomeScrollbar.grid(row = 1, column = 4, sticky = "nsew", rowspan = 6)

outcome.config(yscrollcommand = outcomeScrollbar.set)

# ENTRY BOX
enterExpen = tk.Entry(root, bg = "mintcream")
enterExpen.grid(row = 2, column = 2, sticky = "nsew")

# ADD INCOME BUTTON
add_income = tk.Button(root, text = "ADD INCOME", bg = "mintcream", command = add_income)
add_income.grid(row = 3, column = 2, sticky = "nsew")

# ADD OUTCOME BUTTON
add_outcome = tk.Button(root, text = "ADD OUTCOME", bg = "mintcream", command = add_outcome)
add_outcome.grid(row = 4, column = 2, sticky = "nsew")

# TOTAL
resultLabel = tk.Label(root, text = "Total: ", bg = "thistle")
resultLabel.grid(row = 5, column = 2, sticky = "nsew")

resultVar = tk.StringVar()

result = tk.Entry(root, state = "readonly", bg = "mintcream", textvariable = resultVar)
result.grid(row = 6, column = 2, sticky = "nsew")


root.mainloop()