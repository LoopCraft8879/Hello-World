from tkinter import *

# Create window
root = Tk()
root.title("Calculator")
root.geometry("320x450")
root.resizable(False, False)

# Variable to store expression
expression = ""

# Function to update expression
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate expression
def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

# Function to clear display
def clear():
    global expression
    expression = ""
    equation.set("")

# Display
equation = StringVar()

entry = Entry(root, textvariable=equation, font=("Arial", 20),
              bd=10, relief=RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15)

# Button layout
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
]

# Create buttons
for (text, row, col) in buttons:
    if text == "=":
        Button(root, text=text, width=8, height=3,
               command=equal, bg="lightgreen",
               font=("Arial",12)).grid(row=row, column=col)
    else:
        Button(root, text=text, width=8, height=3,
               command=lambda t=text: press(t),
               font=("Arial",12)).grid(row=row, column=col)

# Clear button
Button(root, text="C", width=35, height=2,
       command=clear, bg="tomato",
       font=("Arial",12)).grid(row=5, column=0, columnspan=4)

# Run application
root.mainloop()
