import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to show calculations and results
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='ridge', justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Function to add text to entry
def btn_click(char):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + char)

# Function to clear entry
def btn_clear():
    entry.delete(0, tk.END)

# Function to calculate result
def btn_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Button layout
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('C',4,2), ('+',4,3),
    ('=',5,0,4)
]

# Create buttons
for btn in buttons:
    text = btn[0]
    row = btn[1]
    col = btn[2]
    colspan = btn[3] if len(btn) > 3 else 1

    action = (lambda x=text: btn_click(x)) if text not in ['C', '='] else None
    if text == 'C':
        action = btn_clear
    elif text == '=':
        action = btn_equal

    b = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=action)
    b.grid(row=row, column=col, columnspan=colspan, sticky="nsew")

# Make buttons expand to fill space
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()