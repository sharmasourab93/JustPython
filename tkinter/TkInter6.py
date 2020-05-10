from tkinter import *
from tkinter import ttk

def get_sum(event):
    num1=int(num1Entry.get())
    num2=int(num2Entry.get())
    sum=num1+num2
    sumEntry.delete(0,"end")
    sumEntry.insert(0,sum)

root=Tk()

num1Entry=Entry(root)
num1Entry.pack(side=LEFT)

Label(root,text="+").pack(side=LEFT)
num2Entry=Entry(root)
num2Entry.pack(side=LEFT)

Label(root,text="=").pack(side=LEFT)
#equalButton.bind("<Button-1>",get_sum)
#equalButton.pack(side=LEFT)

sumEntry=Entry(root)
sumEntry.pack(side=LEFT)

SumButton=Button(root,text="Sum")
SumButton.bind('<Button-1>',get_sum)
SumButton.pack(side=BOTTOM)
root.mainloop()