from tkinter import *

# layout

root = Tk()
root.geometry("300x425")
root.title("Calculator")
root.config(background="black")
root.resizable(False, False)

# function

type = ''
def clear():
    entry.delete(0,END)
    type = ''


def calcu(value):
    global type
    type = type + str(value)
    entry_var.set(type)
    
def equal():
    global type
    eval_type = str(eval(type))
    entry_var.set(eval_type)
    type = ""
# entry

entry_var = StringVar()
entry = Entry(root, font=("Arial", 20), textvariable=entry_var,fg="white", bg="#434c53", justify=RIGHT)
entry.grid(row=0, column=0, columnspan=4, ipady=10)
# button

button_plus = Button(root, text="+",font=("Arial", 20),height=1,width=3, bd=1, fg="black", activeforeground="black", bg="#d0dde6", activebackground="#d0dde6", command=lambda: calcu("+"))
button_minus = Button(root, text="-", font=("Arial", 20),height=1,width=3, bd=1,fg="black", activeforeground="black", bg="#d0dde6", activebackground="#d0dde6", command=lambda: calcu("-"))
button_times = Button(root, text="x",font=("Arial", 20), height=1,width=3, bd=1, fg="black", activeforeground="black", bg="#d0dde6", activebackground="#d0dde6", command=lambda: calcu("*"))
button_div = Button(root, text="÷",font=("Arial", 20),height=1,width=3, bd=1,fg="black", activeforeground="black", bg="#d0dde6", activebackground="#d0dde6", command=lambda: calcu("/"))

button_7 = Button(root, text="7",font=("Arial", 20),height=1,width=3, bd=1, fg="black", activeforeground="black", bg="#d0dde6", activebackground="#d0dde6", command=lambda: calcu("7"))
button_8 = Button(root, text="8", font=("Arial", 20),height=1,width=3, bd=1,fg="black", activeforeground="black", bg="#d0dde6", activebackground="#d0dde6", command=lambda: calcu("8"))
button_9 = Button(root, text="9",font=("Arial", 20), height=1,width=3, bd=1, fg="black", activeforeground="black", bg="#d0dde6", activebackground="#d0dde6", command=lambda: calcu("9"))

button_equal = Button(root, text="=",font=("Arial", 20),height=8,width=3, bd=1,fg="black", activeforeground="black", bg="#ff7076", activebackground="#ff7076", command= equal)

button_4 = Button(root, text="4",font=("Arial", 20),height=1,width=3, bd=1, fg="black", activeforeground="black", bg="#d0dde6", activebackground="#d0dde6", command=lambda: calcu("4"))
button_5 = Button(root, text="5", font=("Arial", 20),height=1,width=3, bd=1,fg="black", activeforeground="black", bg="#d0dde6", activebackground="#d0dde6", command=lambda: calcu("5"))
button_6 = Button(root, text="6",font=("Arial", 20), height=1,width=3, bd=1, fg="black", activeforeground="black", bg="#d0dde6", activebackground="#d0dde6", command=lambda: calcu("6"))

button_1 = Button(root, text="1",font=("Arial", 20),height=1,width=3, bd=1,fg="black", activeforeground="black", bg="#d0dde6", activebackground="#d0dde6", command=lambda: calcu("1"))
button_2 = Button(root, text="2",font=("Arial", 20),height=1,width=3, bd=1, fg="black", activeforeground="black", bg="#d0dde6", activebackground="#d0dde6", command=lambda: calcu("2"))
button_3 = Button(root, text="3", font=("Arial", 20),height=1,width=3, bd=1,fg="black", activeforeground="black", bg="#d0dde6", activebackground="#d0dde6", command=lambda: calcu("3"))

button_0 = Button(root, text="0",font=("Arial", 20), height=1,width=3, bd=1, fg="black", activeforeground="black", bg="#d0dde6", activebackground="#d0dde6", command=lambda: calcu("0"))
button_dot = Button(root, text=".",font=("Arial", 20),height=1,width=3, bd=1,fg="black", activeforeground="black", bg="#d0dde6", activebackground="#d0dde6", command=lambda: calcu("."))
button_c = Button(root, text="c",font=("Arial", 20),height=1,width=3, bd=1,fg="black", activeforeground="black", bg="#d0dde6", activebackground="#d0dde6", command=clear)

# calls button / position

button_plus.grid(row=1, column=0, ipadx=10, ipady=10)
button_minus.grid(row=1, column=1, ipadx=10, ipady=10)
button_times.grid(row=1, column=2, ipadx=10, ipady=10)
button_div.grid(row=1, column=3, ipadx=10, ipady=10)

button_9.grid(row=2, column=0, ipadx=10, ipady=10)
button_8.grid(row=2, column=1, ipadx=10, ipady=10)
button_7.grid(row=2, column=2, ipadx=10, ipady=10)

button_equal.grid(row=2, column=3, rowspan=7, ipadx=10, ipady=10)

button_4.grid(row=3, column=0, ipadx=10, ipady=10)
button_5.grid(row=3, column=1, ipadx=10, ipady=10)
button_6.grid(row=3, column=2, ipadx=10, ipady=10)

button_1.grid(row=4, column=0, ipadx=10, ipady=10)
button_2.grid(row=4, column=1, ipadx=10, ipady=10)
button_3.grid(row=4, column=2, ipadx=10, ipady=10)

button_0.grid(row=5, column=0, ipadx=10, ipady=10)
button_dot.grid(row=5, column=1, ipadx=10, ipady=10)
button_c.grid(row=5, column=2, ipadx=10, ipady=10)

root.mainloop()
