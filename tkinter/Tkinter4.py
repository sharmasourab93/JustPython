#Grid
from tkinter import *
import tkinter.filedialog
from tkinter import ttk

root=Tk()

Label(root,text="First Name").grid(row=0, sticky=E, padx=4)
Entry(root).grid(row=0, column=1, sticky=E, pady=4)

Label(root,text="Last Name").grid(row=0, sticky=E, padx=4)
Entry(root).grid(row=0, column=1, sticky=E, pady=4)


Button(root, text="Submit").grid(row=3)
root.mainloop()