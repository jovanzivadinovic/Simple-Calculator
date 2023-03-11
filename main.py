from tkinter import *
import ttkbootstrap as tb

calculation = ""

def add_to_calc(x):
    global calculation
    calculation+=str(x)

    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate():
    global calculation
    try:
        calculation = str(eval(calculation))
        
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear()
        text_result.insert(1.0, "Error")

def clear():
    global calculation
    calculation = ""

    text_result.delete(1.0, "end")

def backspace():
    global calculation
    calculation=calculation[:-1]

    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)
    





root = tb.Window(themename="vapor")

root.iconbitmap("ikonica.ico")
root.title("Simple Calculator")

text_result = Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

one = Button(root, text="1", command=lambda: add_to_calc(1), width=7, height=2, font=("Arial", 14)).grid(row=2, column=1)
two = Button(root, text="2", command=lambda: add_to_calc(2), width=7,height=2, font=("Arial", 14)).grid(row=2, column=2)
three = Button(root, text="3", command=lambda: add_to_calc(3), width=7,height=2, font=("Arial", 14)).grid(row=2, column=3)
four = Button(root, text="4", command=lambda: add_to_calc(4), width=7,height=2, font=("Arial", 14)).grid(row=3, column=1)
five = Button(root, text="5", command=lambda: add_to_calc(5), width=7,height=2, font=("Arial", 14)).grid(row=3, column=2)
six = Button(root, text="6", command=lambda: add_to_calc(6), width=7,height=2, font=("Arial", 14)).grid(row=3, column=3)
seven = Button(root, text="7", command=lambda: add_to_calc(7), width=7,height=2, font=("Arial", 14)).grid(row=4, column=1)
eight = Button(root, text="8", command=lambda: add_to_calc(8), width=7,height=2, font=("Arial", 14)).grid(row=4, column=2)
nine = Button(root, text="9", command=lambda: add_to_calc(9), width=7,height=2, font=("Arial", 14)).grid(row=4, column=3)
zero = Button(root, text="0", command=lambda: add_to_calc(0), width=7,height=2, font=("Arial", 14)).grid(row=5, column=1)

plus = Button(root, text="+", command=lambda: add_to_calc("+"), width=7,height=2, font=("Arial", 14)).grid(row=2, column=4)
minus = Button(root, text="-", command=lambda: add_to_calc("-"), width=7,height=2, font=("Arial", 14)).grid(row=3, column=4)
mul = Button(root, text="*", command=lambda: add_to_calc("*"), width=7,height=2, font=("Arial", 14)).grid(row=4, column=4)
div = Button(root, text="/", command=lambda: add_to_calc("/"), width=7,height=2, font=("Arial", 14)).grid(row=5, column=4)

open = Button(root, text="(", command=lambda: add_to_calc("("), width=7,height=2, font=("Arial", 14)).grid(row=5, column=2)
closed = Button(root, text=")", command=lambda: add_to_calc(")"), width=7,height=2, font=("Arial", 14)).grid(row=5, column=3)

equals = Button(root, text="=", command=evaluate, width=7, height=2,  font=("Arial", 14)).grid(row=6, column=1)
dot = Button(root, text=".", command=lambda: add_to_calc("."), width=7, height=2, font=("Arial", 14)).grid(row=6, column=2)
back = Button(root, text="<-", command=backspace, width=7, height=2, font=("Arial", 14)).grid(row=6, column=3)
cl = Button(root, text="CLEAR", command=clear, width=7, height=2, font=("Arial", 14)).grid(row=6, column=4)




root.mainloop()