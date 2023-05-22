from tkinter import *

root = Tk()
# add it!!
root.title("simple addition calculator") 

# functions
def numbers(number):
    box.insert(END,number)

def clearing():
    box.delete(0,END)

def addition():
    global addend1
    addend1 = int(box.get())
    box.delete(0,END)

def equals():
    global addend2
    addend2 = int(box.get())
    box.delete(0,END)
    box.insert(0, str(addend1+addend2))


# making the entry box
box = Entry(root, width=15, fg="#ffb3ba")
box.grid(row=0, column=0, columnspan=2)

# and a clear function
clear = Button(root, text="clear", width=5, command=clearing, fg="#ffb3ba")
clear.grid(row=0,column=2)

# making all of the buttons
one = Button(root, text="1", width=5, command=lambda: numbers(1), fg="#ffb347")
two = Button(root, text="2", width=5, command=lambda: numbers(2), fg="#ffb347")
three = Button(root, text="3", width=5, command=lambda: numbers(3), fg="#ffb347")
four = Button(root, text="4", width=5, command=lambda: numbers(4), fg="#ffcc00")
five = Button(root, text="5", width=5, command=lambda: numbers(5), fg="#ffcc00")
six = Button(root, text="6", width=5, command=lambda: numbers(6), fg="#ffcc00")
seven = Button(root, text="7", width=5, command=lambda: numbers(7), fg="#addfac")
eight = Button(root, text="8", width=5, command=lambda: numbers(8), fg="#addfac")
nine = Button(root, text="9", width=5, command=lambda: numbers(9), fg="#addfac")
zero = Button(root, text="0", width=5, command=lambda: numbers(0), fg="#bae1ff")

one.grid(row=1, column=0)
two.grid(row=1,column=1)
three.grid(row=1,column=2)

four.grid(row=2,column=0)
five.grid(row=2,column=1)
six.grid(row=2,column=2)

seven.grid(row=3,column=0)
eight.grid(row=3,column=1)
nine.grid(row=3,column=2)

zero.grid(row=4,column=0)

# operation buttons
add = Button(root,text="+", width=5, command=addition, fg="#bae1ff")
equal = Button(root,text="=",width=5, command=equals, fg="#bae1ff")

add.grid(row=4,column=1)
equal.grid(row=4,column=2)


root.mainloop()
