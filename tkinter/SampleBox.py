from tkinter import *
from tkinter import ttk
root=Tk()
def print_sum():
    print("Hello Button WOrld")
Label(root,text="Sourab S Sharma").grid(row=0,column=0,sticky=E)
Entry(root,width=50).grid(row=0,column=1,sticky=E)
B1=Button(root,text="Submit").grid(row=1,column=0)
print(type(B1))
B1.bind('<Button-1>',print_sum)
B1.pack()

root.mainloop()