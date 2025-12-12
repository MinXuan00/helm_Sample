import tkinter as tk

# Function to update the expression
def press(key):
    entry_var.set(entry_var.get() + str(key))

# Function to evaluate the expression
def equal():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Error")

# Function to clear the entry
def clear():
    entry_var.set("")

# Main window
root = tk.Tk()
root.title("Calculator")

# Entry field
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=('Arial', 20), bd=10, relief='sunken', justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=equal)
    elif text == "C":
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=clear)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=lambda t=text: press(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
