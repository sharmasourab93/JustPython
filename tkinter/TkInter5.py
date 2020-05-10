from tkinter import *
from tkinter import ttk
root=Tk()
Label(root, text="Description").grid(row=0, column=0, sticky=W)
Entry(root,width=50).grid(row=0,column=8)
Button(root,text="Submit").grid(row=0,column=9)

Label(root, text="Quality").grid(row=2, column=0, sticky=W)
Radiobutton(root,text="New",value=1).grid(row=3,column=0,sticky=W)
Radiobutton(root,text="Old",value=2).grid(row=3,column=1,sticky=W)
Radiobutton(root,text="Good",value=3).grid(row=3,column=2,sticky=W)
Radiobutton(root,text="Poor",value=4).grid(row=3,column=3,sticky=W)

Label(root,text="Benefits").grid(row=1,column=1,sticky=W)
Checkbutton(root,text="Free Shipping").grid(row=2,column=1,sticky=W)
Checkbutton(root,text="Bonus Gift").grid(row=2,column=2,sticky=W)


root.mainloop()