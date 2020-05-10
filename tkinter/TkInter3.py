from tkinter import *
from tkinter import ttk

root=Tk()

frame= Frame(root)

Label(frame, text="A Bunch of Buttons").pack()

Button(frame, text="B1").pack(side=LEFT, fill=Y)
Button(frame, text="B2").pack(side=TOP, fill=X)
Button(frame, text="B1").pack(side=RIGHT, fill=X)
Button(frame, text="B1").pack(side=LEFT, fill=X)
frame.pack()

root.mainloop()