from tkinter import *

root = Tk()
root.geometry('1366x768')
root.resizable(0, 0)
root.title('MY FIRST CALCULATOR')
statement = Label(root)

def add():
    x=int(firstEntry.get())
    y=int(secondEntry.get())
    global statement
    statement.destroy()
    a=x+y
    statement = Label(text=f"{nameEntry.get()} your addition of two number is  {a}.")
    statement.grid(row=9, column=5, pady=25)

def subtract():
    x=int(firstEntry.get())
    y=int(secondEntry.get())
    global statement
    statement.destroy()
    a=x-y
    statement = Label(text=f" {nameEntry.get()} your subtract of two number is {a}.")
    statement.grid(row=10, column=5, pady=25)

def multiply():
    x=int(firstEntry.get())
    y=int(secondEntry.get())
    global statement
    statement.destroy()
    a=x*y
    statement = Label(text=f" {nameEntry.get()} your multiplication of two number is {a}.")
    statement.grid(row=11, column=5, pady=25)

def divide():
    x=int(firstEntry.get())
    y=int(secondEntry.get())
    global statement
    statement.destroy()
    a=x%y
    statement = Label(text=f" {nameEntry.get()} your division of two number is {a}.")
    statement.grid(row=12, column=5, pady=25)

l1 = Label(text="Name: ")
l1.grid(row=1, column=0)
nameValue = StringVar()

nameEntry = Entry(root, textvariable=nameValue)
nameEntry.grid(row=1, column=1, padx=25, pady=15)

l2 = Label(text="input : ")
l2.grid(row=2, column=0)
firstValue = StringVar()
firstEntry = Entry(root, textvariable=firstValue)
firstEntry.grid(row=2, column=1, padx=25, pady=15)

l3 = Label(text="second : ")
l3.grid(row=3, column=0)
secondValue = StringVar()
secondEntry = Entry(root, textvariable=secondValue)
secondEntry.grid(row=3, column=1, padx=25, pady=15)

button = Button(text="+",command=add )
l4 = Label(text="Addition")
l4.grid(row=4,column=0)
button.grid(row=4, column=1)


button = Button(text="-",command=subtract)
l5 = Label(text="Subtraction")
l5.grid(row=5,column=0)
button.grid(row=5, column=1)


button = Button(text="*", command=multiply)
l6 = Label(text="Multiplication")
l6.grid(row=6,column=0,)
button.grid(row=6, column=1)



button = Button(text="%", command=divide)
l7 = Label(text="Division")
l7.grid(row=7,column=0)
button.grid(row=7, column=1)
root.mainloop()

# button_dict={}
# option= ["+", "-", "*", "%"]

# for i in option:
#    def func(x=i):
#       return entry_update(x)

#    button_dict[i]=Tk.Button(text=i, command= func)
#    button_dict[i].pack()


