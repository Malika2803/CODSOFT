# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 14:18:08 2023

@author: User
"""

from tkinter import *
from tkinter import messagebox


r = Tk()
r.geometry("420x500+400+100")
r.configure(bg="slate gray")
r.title('Calculator')
r.resizable(0, 0)


def b_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, str(current) + str(number))
    
    
def b_clear():
    entry.delete(0, END)


def b_equal():
    expression = entry.get()
    result = eval(expression)
    entry.delete(0, END)
    entry.insert(END, result)
    
    
def b_close():
    confirm = messagebox.askyesno("Confirm completed", "Are you sure you want to EXIT?")
    if confirm:
        r.destroy()
    else:
        pass
    

entry = Entry(r, font="30",bg='snow3',borderwidth=2,justify = RIGHT)
entry.place(x=30, y=50, width=350, height=50)

flm2 = Frame(r, width = 500, height = 372.5, bg = "teal")
flm2.place(x=0,y=130)

button_1 = Button(flm2, text="1", font="30", command=lambda: b_click(1))
button_1.place(x=20, y=130, width=80, height=50)

button_2 = Button(flm2, text="2", font="30", command=lambda: b_click(2))
button_2.place(x=120, y=130, width=80, height=50)

button_3 = Button(flm2, text="3", font="30", command=lambda: b_click(3))
button_3.place(x=220, y=130, width=80, height=50)

button_4 = Button(flm2, text="4", font="30", command=lambda: b_click(4))
button_4.place(x=20, y=190, width=80, height=50)

button_5 = Button(flm2, text="5", font="30", command=lambda: b_click(5))
button_5.place(x=120, y=190, width=80, height=50)

button_6 = Button(flm2, text="6", font="30", command=lambda: b_click(6))
button_6.place(x=220, y=190, width=80, height=50)

button_7 = Button(flm2, text="7", font="30", command=lambda: b_click(7))
button_7.place(x=20, y=250, width=80, height=50)

button_8 = Button(flm2, text="8", font="30", command=lambda: b_click(8))
button_8.place(x=120, y=250, width=80, height=50)

button_9 = Button(flm2, text="9", font="30", command=lambda: b_click(9))
button_9.place(x=220, y=250, width=80, height=50)

button_0 = Button(flm2, text="0", font="30", command=lambda: b_click(0))
button_0.place(x=120, y=310, width=80, height=50)

button_plus = Button(flm2, text="+", font="30",bg='green', command=lambda: b_click('+'))
button_plus.place(x=320, y=250, width=80, height=50)

button_minus = Button(flm2, text="-", font="30",bg='green', command=lambda: b_click('-'))
button_minus.place(x=320, y=190, width=80, height=50)

button_multiply = Button(flm2, text="x", font="30",bg='green', command=lambda: b_click('*'))
button_multiply.place(x=320, y=130, width=80, height=50)

button_divide = Button(flm2, text="÷", font="30",bg='green', command=lambda: b_click('/'))
button_divide.place(x=320, y=70, width=80, height=50)

button_clear = Button(flm2, text="Clear", font="30",bg='olive', command=b_clear)
button_clear.place(x=20, y=70, width=280, height=50)

button_equal = Button(flm2, text="=", font="30",bg='olive', command=b_equal)
button_equal.place(x=220, y=310, width=180, height=50)

button_close = Button(flm2, text="EXIT", font="30",bg='red', command=b_close)
button_close.place(x=20, y=310, width=80, height=50)

mainloop()